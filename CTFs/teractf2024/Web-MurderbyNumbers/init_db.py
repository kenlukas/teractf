import sqlite3

db = sqlite3.connect('database.db')
with open('schema.sql') as f:
  db.cursor().executescript(f.read(), )
db.commit()

cur = db.cursor()

cur.execute("INSERT INTO crows (filename) VALUES (?)",
            ('bird_on_a_wire.jpg')
            )

cur.execute("INSERT INTO crows (filename) VALUES (?)",
            ('bird_on_a_fence.jpg')
            )

cur.execute("INSERT INTO crows (filename) VALUES (?)",
            ('disco_birds.jpg')
            )

cur.execute("INSERT INTO crows (filename) VALUES (?)",
            ('')
            )

cur.execute("INSERT INTO crows (filename) VALUES (?)",
            ('counting_crows.jpg')
            )

db.commit()
db.close()
