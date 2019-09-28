import sqlite3

conn = sqlite3.connect('notas.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO notas (chave, status)  VALUES (?,?)",  ('11111','1') )
cursor.execute("INSERT INTO notas (chave, status)  VALUES (?,?)",  ('22222','1') )
cursor.execute("INSERT INTO notas (chave, status)  VALUES (?,?)",  ('33333','1') )
cursor.execute("INSERT INTO notas (chave, status)  VALUES (?,?)",  ('44444','1') )
cursor.execute("INSERT INTO notas (chave, status)  VALUES (?,?)",  ('55555','1') )

conn.commit()
