import sqlite3

def init_db():
 conn = sqlite3.connect('notas.db')
 cursor = conn.cursor()
 cursor.execute("DROP TABLE IF EXISTS notas")
 cursor.execute("CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY, chave TEXT, cnpj TEXT, data TEXT, uf TEXT, numero TEXT, modelo TEXT, serie TEXT, tipo_emissao TEXT, codigo TEXT, status TEXT, valor REAL, message TEXT ) ")
 conn.commit()
 conn.close()
