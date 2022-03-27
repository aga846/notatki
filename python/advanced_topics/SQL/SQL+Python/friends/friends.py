import sqlite3
conn = sqlite3.connect("my_friends.db")

c = conn.cursor()
c.execute("CREATE TABLE friends(first_name TEXT, last_name TEXT, closeness INTEGER);")
conn.commit()
conn.close()
