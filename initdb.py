import sqlite3
conn = sqlite3.connect('notas.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS notas")
cursor.execute("CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY, chave TEXT, cnpj TEXT, data TEXT, uf TEXT, numero TXT, modelo TEXT, serie TXT, tipo_emissao TXT, codigo TXT, status TEXT, valor REAL, message TEXT ) ")
conn.commit()