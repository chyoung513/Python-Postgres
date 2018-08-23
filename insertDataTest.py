import csv
import psycopg2

conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor()

with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    for line in reader:
        cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (line[0], line[1], line[2], line[3]))

cur.execute("SELECT * from users")
users = cur.fetchall()

conn.close()
        
    
