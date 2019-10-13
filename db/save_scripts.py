import sqlite3

def save_config():
 conn = sqlite3.connect('notas.db')
 
 cursor = conn.cursor()
 #cursor.execute("DELETE FROM scripts")
 #cursor.execute("DELETE FROM steps")
 
 #name TEXT, description TEXT, version TEXT DEFAULT '1', status TEXT DEFAULT '0', delete_on_sync TEXT DEFAULT '0'
 #cursor.execute("INSERT INTO scripts (name, description, version, status, delete_on_sync)  VALUES (?,?,?,?,?)",  ('Cupom sem CPF com Chave', 'Opção no menu de cadastro de cupons sem CPF, informando a chave de acesso', '1', '1','1'  ) )
 #cursor.execute("INSERT INTO scripts (name, description, version, status, delete_on_sync)  VALUES (?,?,?,?,?)",  ('Cadastramento cupom autorizado entidade', 'Opção no menu de cadastramento de cupons informando chave de acesso, quando autorizado pela instituição', '1', '1','1'  ) )

 conn.commit()
 conn.close()




if __name__ == "__main__":
    save_config()