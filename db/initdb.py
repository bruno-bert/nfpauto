import sqlite3

def init_db():
 conn = sqlite3.connect('notas.db')
 cursor = conn.cursor()
 
 #tabela de notas
 cursor.execute("DROP TABLE IF EXISTS notas")
 cursor.execute("CREATE TABLE IF NOT EXISTS notas (id INTEGER PRIMARY KEY, chave TEXT, cnpj TEXT, data TEXT, uf TEXT, numero TEXT, modelo TEXT, serie TEXT, tipo_emissao TEXT, codigo TEXT, status TEXT, valor REAL, message TEXT ) ")

 #tabela de cnpjs
 cursor.execute("DROP TABLE IF EXISTS cnpj")
 cursor.execute("CREATE TABLE IF NOT EXISTS cnpj (id INTEGER PRIMARY KEY, cnpj TEXT, empresa TEXT, uf TEXT, modelo TEXT, serie TEXT ) ")

 #tabela de cnpj padrao
 cursor.execute("DROP TABLE IF EXISTS cnpj_padrao")
 cursor.execute("CREATE TABLE IF NOT EXISTS cnpj_padrao (id INTEGER PRIMARY KEY, cnpj TEXT  ) ")

 #tabela configura arquivo
 cursor.execute("DROP TABLE IF EXISTS config_arquivo")
 cursor.execute("CREATE TABLE IF NOT EXISTS config_arquivo (id INTEGER PRIMARY KEY, cnpj TEXT, id_text TEXT, nome TEXT, delimitador TEXT, tipo TEXT, coluna INTEGER, nome_coluna TEXT, header TEXT   ) ")

 #tabela configura arquivo padrão
 cursor.execute("DROP TABLE IF EXISTS config_arquivo_padrao")
 cursor.execute("CREATE TABLE IF NOT EXISTS config_arquivo_padrao (id INTEGER PRIMARY KEY, id_text TEXT ) ")


 

 conn.commit()
 conn.close()

def limpa_notas_db():
 conn = sqlite3.connect('notas.db')
 cursor = conn.cursor()
 cursor.execute("delete from notas")
 conn.commit()
 conn.close()

def limpa_cnpj_db():
 conn = sqlite3.connect('notas.db')
 cursor = conn.cursor()
 cursor.execute("delete from cnpj")
 conn.commit()
 conn.close()


if __name__ == "__main__":
    init_db()