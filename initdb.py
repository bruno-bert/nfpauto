import sqlite3
conn = sqlite3.connect('notas.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS notas")
cursor.execute("CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY, chave TEXT, cnpj TEXT, valor REAL, data TEXT, status TEXT ) ")
conn.commit()