import sqlite3

def save_config():
 conn = sqlite3.connect('notas.db')
 
 cursor = conn.cursor()
 cursor.execute("DELETE FROM config_arquivo")
 cursor.execute("DELETE FROM config_arquivo_padrao")
 
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'TEXT_PADRAO', 'Padrão', None, 'txt', '0','','0'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'TEXT_MULT_COL', 'Múltiplas Colunas', ',', 'txt', '4','','0'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'TEXT_MULT_COL_HEADER', 'Múltiplas Colunas com Header', ',', 'txt', '4','','1'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'CSV', 'Csv', ',', 'csv', '4','','0'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'CSV_HEADER', 'Csv com Header e Ponto e Vírgula', ';', 'csv', '4','','1'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'EXCEL', 'Excel sem Header', '', 'excel', '4','','0'  ) )
 cursor.execute("INSERT INTO config_arquivo (cnpj, id_text, nome, delimitador, tipo, coluna, nome_coluna, header)  VALUES (?,?,?,?,?,?,?,?)",  ('*', 'EXCEL_HEADER', 'Excel com Header', '', 'excel', '4','Chave','1'  ) )

 cursor.execute("INSERT INTO config_arquivo_padrao (id_text)  VALUES ('{}')".format('TEXT_PADRAO')  )


 conn.commit()
 conn.close()




if __name__ == "__main__":
    save_config()