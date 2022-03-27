import sqlite3
conn = sqlite3.connect("my_friends.db")

# creating a cursor
c = conn.cursor()

# selecting all with for loop
c.execute("SELECT * FROM friends")
for result in c:
    print(result)

# selecting all with fetchall()    
c.execute("SELECT * FROM friends")
print(c.fetchall())

# selecting one type of data - the first occurence
c.execute("SELECT * FROM friends WHERE first_name IS 'Ania'")
print(c.fetchone())

conn.commit()
conn.close()
