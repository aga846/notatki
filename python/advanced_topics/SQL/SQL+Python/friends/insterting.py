import sqlite3
conn = sqlite3.connect("my_friends.db")

c = conn.cursor()

# inserting  
data = ("Marta", "Min", 6)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

# bulk inserts
people = [
  ("Kasia", "Pal", 10),
  ("Ania", "Piet", 8),
  ("Asia", "Roz", 7),
  ("Dorota", "Woj", 7)
]

c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

conn.commit()
conn.close()
