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
 cursor.execute("CREATE TABLE IF NOT EXISTS config_arquivo (id INTEGER PRIMARY KEY, cnpj TEXT, id_text TEXT, nome TEXT, delimitador TEXT, tipo TEXT, coluna INTEGER, nome_coluna TEXT, header TEXT, sheet_name TEXT   ) ")

 #tabela configura arquivo padrão
 cursor.execute("DROP TABLE IF EXISTS config_arquivo_padrao")
 cursor.execute("CREATE TABLE IF NOT EXISTS config_arquivo_padrao (id INTEGER PRIMARY KEY, id_text TEXT ) ")

 #tabela script automation
 #cursor.execute("DROP TABLE IF EXISTS scripts")
 #cursor.execute("CREATE TABLE IF NOT EXISTS scripts (id INTEGER PRIMARY KEY, name TEXT, description TEXT, version TEXT DEFAULT '1', status TEXT DEFAULT '0', delete_on_sync TEXT DEFAULT '0' ) ")

  #tabela steps automation
 #cursor.execute("DROP TABLE IF EXISTS steps")
 #cursor.execute("CREATE TABLE IF NOT EXISTS steps (id INTEGER PRIMARY KEY, script_id INTEGER, step_id INTEGER, step_name TEXT, step_description TEXT, sort_number INTEGER DEFAULT 0, skip TEXT DEFAULT '0', on_success_goto INTEGER DEFAULT 0, on_error_goto INTEGER DEFAULT 0, steps_to_skip_on_next_run TEXT, find_method TEXT, expression TEXT, action TEXT, text_to_type TEXT, check_session TEXT DEFAULT '1', is_check_session_timeout TEXT DEFAULT '0', session_timeout__step_id INTEGER, on_session_timeout_start_from INTEGER, base_element TEXT, element_from_step INTEGER, error_message_finder TEXT, success_message_finder TEXT, must_wait_element TEXT default '1', timeout_to_element INTEGER, log_message_before TEXT, log_message_after TEXT, wait_manual_action TEXT DEFAULT '0', steps_to_skip_on_next_run TEXT , is_end_step TEXT, manual_action_message TEXT, CONSTRAINT fk_script  FOREIGN KEY (script_id) REFERENCES scripts (id) ON DELETE CASCADE ) ")




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