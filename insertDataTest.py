import psycopg2

conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor();

#user_accounts.csv has a header row
#load the file and copy it to database
with open('user_accounts.csv', 'r') as f:
    #skip header row
    next(f)
    cur.copy_from(f, 'users', sep=',')

cur.execute("SELECT * FROM users;")
users = cur.fetchall()

conn.close()
