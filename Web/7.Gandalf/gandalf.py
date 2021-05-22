from flask import render_template, redirect, url_for, request, flash, abort
from main import app
from hashlib import sha256
import sqlite3
import re
from datetime import datetime

QUERY_LOGIN = "SELECT page_id FROM users WHERE username=? AND password=?;"
QUERY_REGISTRATION_USER = "SELECT username FROM users WHERE username=?;"
QUERY_REGISTRATION_PAGE = "SELECT page_id FROM users WHERE page_id=?;"
QUERY_REGISTRATION_INSERT = "INSERT INTO users(username, password, page_id) VALUES (?, ?, ?);"
QUERY_NOTES = "SELECT content FROM notes WHERE page_id=? ORDER BY timestamp DESC;"
QUERY_PAGE = "SELECT page_id FROM users WHERE page_id=?;"
QUERY_ADD_NOTE = "INSERT INTO notes(content, page_id, timestamp) VALUES (?, ?, ?);"
QUERY_DELETE_NOTES = "DELETE FROM notes WHERE page_id=?;"

db_conn = None
db_cur = None


def has_numbers(input_str):
    return any(char.isdigit() for char in input_str)

def you_shall_not_pass_lvl3(note):
    n = len(note)
    new_note = ""
    for i in range(n):
        if note[i] == '<':
            stack = 1
            for j in range(i + 1, n):
                if note[j] == '<':
                    stack += 1
                elif note[j] == '>':
                    stack -= 1
                if stack == 0:
                    break
            if stack == 0:
                for k in range(n):
                    if(k < i or k > j):
                        new_note += note[k]
                return you_shall_not_pass_lvl3(new_note)
    return note

def you_shall_not_pass_lvl2(note):
    re_lvl2 = re.compile(re.escape('script'), re.IGNORECASE)
    note = re_lvl2.sub('', note)
    return you_shall_not_pass_lvl3(note)

def you_shall_not_pass_lvl1(note):
    re_lvl1 = re.compile(re.escape('javascript'), re.IGNORECASE)
    note = re_lvl1.sub('', note)
    return you_shall_not_pass_lvl2(note)

@app.before_request
def initapp():
    global db_conn
    global db_cur
    db_conn = sqlite3.connect('db/gandalf.db')
    db_cur = db_conn.cursor()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    global db_cur
    global db_conn
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        login = request.form.get('login', '')
        register = request.form.get('register', '')
        if login == "login":
            db_cur.execute(QUERY_LOGIN, (username, password))
            rows = db_cur.fetchall()
            if not rows:
                flash(' %s is not registered!' % username, 'danger')
                return redirect(url_for('login'))
            if len(rows) == 1:
                return redirect(url_for('notes', pageid=rows[0]))
        elif register == "register":
            db_cur.execute(QUERY_REGISTRATION_USER, (username, ))
            rows = db_cur.fetchall()
            if rows:
                flash('%s is already registered!' % username, 'danger')
                return redirect(url_for('login'))
            str_to_hash = (username + "_" + password).encode('utf-8')
            page_id = sha256(str_to_hash).hexdigest().upper()
            db_cur.execute(QUERY_REGISTRATION_PAGE, (page_id,))
            rows = db_cur.fetchall()
            if rows:
                flash('%s is already registered!' % username, 'danger')
                return redirect(url_for('login'))
            if len(password) < 8:
                flash('Password must be at least 8 characters long!', 'danger')
                return redirect(url_for('login'))
            if not has_numbers(password):
                flash('Password must contain at least 1 number!', 'danger')
                return redirect(url_for('login'))
            db_cur.execute(QUERY_REGISTRATION_INSERT, (username, password, page_id))
            db_conn.commit()
            flash(' %s successfully registerd!' % username, 'success')
            return redirect(url_for('login'))
    flash('There was something wrong about last request I got.')
    return redirect(url_for('login'))

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    global db_cur
    global db_conn
    page_id = request.args.get('pageid')
    if page_id == "":
        abort(404)
    db_cur.execute(QUERY_PAGE, (page_id,))
    rows = db_cur.fetchall()
    if not rows:
        abort(404)
    db_cur.execute(QUERY_NOTES, (page_id,))
    rows = db_cur.fetchall()
    notes = []
    for elem in rows:
        notes.append(elem[0])
    if request.method == 'GET':
        return render_template('notes.html', notes=notes)
    elif request.method == 'POST':
        add_note = request.form.get('add_note', '')
        clear_notes = request.form.get('clear_notes', '')
        if add_note == "add_note":
            if len(notes) > 9:
                flash('No more notes!', 'danger')
                return redirect(url_for('notes', pageid=page_id))                
            note = request.form.get('note', '')
            note = you_shall_not_pass_lvl1(note)
            if note != "" and len(note) < 500:
                db_cur.execute(QUERY_ADD_NOTE, (note, page_id, datetime.now()))
                db_conn.commit()
                flash('Note correctly added.', 'success')
            return redirect(url_for('notes', pageid=page_id))
        elif clear_notes == "clear_notes":
            db_cur.execute(QUERY_DELETE_NOTES, (page_id, ))
            db_conn.commit()
            flash('Notes deleted.', 'success')
            return redirect(url_for('notes', pageid=page_id))
    flash('There was something wrong about last request I got.')
    return redirect(url_for('login'))