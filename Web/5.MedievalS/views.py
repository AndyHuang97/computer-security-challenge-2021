from flask import session, render_template, request, redirect, url_for, flash, abort, jsonify
from main import app
import time
import math
import json

db = None

CLASSTYPES = ["Swordman", "Cleric", "Wizard", "Dragon"]
FADEOUTSECS = 30
maps = {}
descriptions = {}
secrets = {}

class NPC():
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel


class Map():
    def __init__(self, name, allow=CLASSTYPES):
        self.name = name
        self.users = []
        self.msgs = []
        self.allow = allow

    def add_user(self, user):
        self._delete_old_users()
        if user not in self.users:
            self.users.append(user)

    def add_msg(self, msg, user):
        self.add_user(user)
        self.msgs.append({'time': time.time(), 'user': user, 'msg': msg})

    def to_dict(self):
        return self.__dict__

    def _delete_old_users(self):
        new_userlist = []
        for u in self.users:
            for m in sorted(self.msgs, key=lambda x: x['time'], reverse=True):
                if (m['time'] + FADEOUTSECS) < time.time():
                    break
                elif u == m['user']:
                    new_userlist.append(u)
                    break
        self.users = new_userlist


class User():
    def __init__(self, username, classType):
        self.username = username
        self.classType = classType
        self.level = 0
        self.exp = 0

    def add_exp(self, i):
        self.exp += i
        old_lv = self.level
        self.level = int(math.log(self.exp, 2))
        if old_lv != self.level:
            flash('Congrats you ard now lv %d!' % self.level)

    def to_dict(self):
        return self.__dict__
        return {'username': self.username, 'classType': self.classType, 'level': self.level, 'exp': self.exp}

    @classmethod
    def from_dict(cls, d):
        u = User(d['username'], d['classType'])
        u.level = d['level']
        u.exp = d['exp']
        return u

def load_secrets():
    global secrets
    with open("data/secrets.json") as f:
        secrets = json.load(f)

def get_flag_from_user(username):
    return secrets.get(username, "No Secret!")

def get_current_user():
    current_user = None
    if 'user' in session:
        current_user = User.from_dict(session['user'])
    return current_user


def update_current_user(u):
    session['user'] = u.to_dict()

def load_descriptions():
    descriptions['forests'] = open("./data/forests").read().split("---")
    descriptions['cities'] = open("./data/cities").read().split("---")
    descriptions['dungeons'] = open("./data/dungeons").read().split("---")

def compute_hash(s, maxval):
    r = 0
    for c in s:
        r += ord(c)
    return r % maxval


@app.before_first_request
def initializegame():
    #load_descriptions()
    #load_secrets()
    dname = "Unbelievable Dungeon"
    dungeon = Map(dname, ["Dragon"])
    maps[dname] = dungeon
    dungeon.add_msg("Hey fella Dragon.", "The Dragon")

    wname = "Central City"
    map = Map(wname)
    maps[wname] = map
    map.add_msg("Let's get some Adventure!", "Funny Guy")
    map.add_msg("Looks like our Creator is a copypaster. I think he should not do that.", "Serious Guy")

    wname = "WizTown"
    map = Map(wname, ["Wizard"])
    maps[wname] = map
    map.add_msg("Welcome to WizTown. have you herd of %s? It's a place full of magic." % dname, "Gandalf")

    wname = "SwordCity"
    map = Map(wname, ["Swordman"])
    maps[wname] = map
    map.add_msg("Bring your sword and let's slay some dragons at %s." % dname, "Cloud")

    wname = "Saint Village"
    map = Map(wname, ["Cleric"])
    maps[wname] = map
    map.add_msg("Our god lives in %s." % dname, "Don Tbreak")

    wname = "Unbelievable Woods"
    woods = Map(wname)
    maps[wname] = woods
    woods.add_msg("I'm going home at %s" % dname, "The Dragon")


@app.template_filter('mapdescription')
def caps(text):
    """Convert a name to its description."""
    if "wood" in text.lower() or "forest" in text.lower():
        return descriptions['forests'][compute_hash(text, len(descriptions['forests']))]
    if "city" in text.lower() or "town" in text.lower() or "village" in text.lower():
        des = descriptions['cities'][compute_hash(text, len(descriptions['cities']))]
        des = des.replace("%s", text)
        return des
    if "dungeon" in text.lower() or "cave" in text.lower():
        return descriptions['dungeons'][compute_hash(text, len(descriptions['dungeons']))]

    return "An insignificat place to be."


@app.route('/')
def index():
    u = get_current_user()
    available_places = []
    if u is not None:
        available_places = [maps[m] for m in maps if u.classType in maps[m].allow]
    return render_template('index.html', current_user=u, maps=available_places)


@app.route('/map/<place>')
def map(place):
    u = get_current_user()
    if place not in maps:
        maps[place] = Map(place)
    maps[place].add_msg("Here I am!", u.username)
    maps[place].add_user(u.username)
    if place == "Unbelievable Dungeon" and maps[place].allow:
        if u.level >= 99:
            maps[place].add_msg("Dear %s, I have a secret for you %s" % (u.username, get_flag_from_user(u.username)), "The Dragon")
        else:
            maps[place].add_msg("Dear %s, I am not giving my secrets to week creatures like you." % (u.username,), "The Dragon")

    return render_template('map.html', place=place, current_user=u, allowed=maps[place].allow)


@app.route('/chat/<place>')
def chat(place):
    if place in maps:
        u = get_current_user()
        map = maps[place]
        if u.classType in map.allow:
            return jsonify(map.to_dict())
        else:
            return "You cannot enter here."
    else:
        return "Map not found."


@app.route('/chat/msg/<place>', methods=['POST'])
def postMsg(place):
    if request.method != 'POST':
        return abort(404)
    if place not in maps:
        return abort(404)

    u = get_current_user()
    msg = request.json.get('msg', '')
    if msg == "":
        return abort(404)
    maps[place].add_msg(msg, u.username)
    u.add_exp(1)
    update_current_user(u)
    resp = jsonify(success=True)
    return resp


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        get_current_user()
        return render_template('login.html')

    elif request.method == 'POST':
        username = request.form.get('username', '')
        classType = request.form.get('class', '')
        if not (classType in CLASSTYPES[:-1]):
            flash('You cannot be a %s' % classType, category='warning')
            if not(classType in CLASSTYPES):
                flash('%ss do not exists in this realm. ' % classType, category='danger')
            return redirect(url_for('login'))
        u = User(username, classType)
        update_current_user(u)
        flash('Welcome to Medivals!')
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    del session['user']
    flash('Real life sucks! Come back!')
    return redirect(url_for('index'))