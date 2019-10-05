import sqlite3

def save_config():
 conn = sqlite3.connect('notas.db')
 
 cursor = conn.cursor()
 cursor.execute("DELETE FROM config_arquivo")
 
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'TEXT_PADRAO', 'Padrão', None, 'txt', '1','','0'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'TEXT_MULT_COL', 'Múltiplas Colunas', ',', 'txt', '5','','0'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'TEXT_MULT_COL_HEADER', 'Múltiplas Colunas com Header', ',', 'txt', '5','','1'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'CSV', 'Csv', ',', 'csv', '5','','0'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'CSV_HEADER', 'Csv com Header e Ponto e Vírgula', ';', 'csv', '5','','1'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'EXCEL', 'Excel sem Header', '', 'xls|xlsx', '5','','0'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'EXCEL_HEADER', 'Excel com Header', '', 'xls|xlsx', '','Chave','1'  ) )

 conn.commit()
 conn.close()




if __name__ == "__main__":
    save_config()