import sqlite3
conn = sqlite3.connect("users.db")

c = conn.cursor()
query = "CREATE TABLE users (username TEXT, password TEXT);"
c.execute(query)

users_and_pass = [
    ("Aga", "kocham_damiana"),
    ("Damian", "kocham_age"),
    ("Kot", "meow")
]

c.executemany("INSERT INTO users VALUES (?,?)", users_and_pass)


conn.commit()
conn.close()
