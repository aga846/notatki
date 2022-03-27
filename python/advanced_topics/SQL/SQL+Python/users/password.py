import sqlite3
conn = sqlite3.connect("users.db")

u = input("please enter your username... ")
p = input("please enter your password... ")
query = f"SELECT * FROM users WHERE username='{u}' AND password='{p}'"

c = conn.cursor()
c.execute(query)

result = c.fetchone()
if result:
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")

conn.commit()
conn.close()
