import sqlite3

def update_config():
 conn = sqlite3.connect('notas.db')
 
 #alterar aqui para o tipo de importacao padrao
 id_text='EXCEL'

 cursor = conn.cursor()
 cursor.execute("DELETE FROM config_arquivo_padrao")
 cursor.execute("INSERT INTO config_arquivo_padrao (id_text)  VALUES ('{}')".format(id_text))


 conn.commit()
 conn.close()




if __name__ == "__main__":
    update_config()