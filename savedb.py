import sqlite3

conn = sqlite3.connect('notas.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO notas (chave, status)  VALUES (?,?)",  ('11111','1') )

conn.commit()
