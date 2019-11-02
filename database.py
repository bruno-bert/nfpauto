import sqlite3

import constant
import messages


def atualiza_status_nota(chave, status):
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_UPDATE_STATUS_NOTA.format(status, chave)
 cursor = conn.cursor()
 cursor.execute(query)
 conn.commit()
 conn.close()

def atualiza_status_message_nota(chave, status, message):
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_UPDATE_STATUS_MESSAGE_NOTA.format(status, message, chave)
 cursor = conn.cursor()
 cursor.execute(query)
 conn.commit()
 conn.close()

def busca_cnpj_padrao():
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_SELECT_CNPJ_PADRAO
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchone()
 conn.close()
 return rows

def busca_config_arquivo(id):
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_SELECT_CONFIG_ARQUIVO.format(id)
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchone()
 conn.close()
 return rows 
 
def busca_config_arquivo_padrao():
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_SELECT_CONFIG_ARQUIVO_PADRAO
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchone()
 conn.close()
 return rows

def busca_script_padrao():
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_SELECT_SCRIPT_PADRAO
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchone()
 conn.close()
 return rows   

def busca_cnpj_padrao_valor():
 rows = busca_cnpj_padrao()
 if (rows):
  for row_data in rows:    
   cnpj = row_data  
  return cnpj
 else:
  return constant.EMPTY_STR


def salva_cnpj_padrao_banco(cnpj):
 conn = sqlite3.connect('notas.db')
 existe_cnpj = busca_cnpj_padrao_valor()
 query = constant.QUERY_UPDATE_CNPJ_PADRAO if existe_cnpj else constant.QUERY_INSERT_CNPJ_PADRAO
 cursor = conn.cursor()
 query = query.format(cnpj)
 print("query: {}".format(query))
 cursor.execute(query )
 conn.commit() 
 conn.close()

def busca_chaves_banco():
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_SELECT_NOTAS_PRINCIPAL
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 return rows

def busca_chaves_por_status(status):
 conn = sqlite3.connect('notas.db')
 query = "select * from notas where status = {}".format(status)
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 return rows



def busca_cnpj_banco():
 conn = sqlite3.connect('notas.db')
 query = "select * from cnpj"
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 return rows 

def salva_chave_banco(new_nota):
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute(constant.QUERY_SAVE,  
                    (new_nota.chave, 
                     new_nota.cnpj, 
                     new_nota.data, 
                     new_nota.uf, 
                     new_nota.numero, 
                     new_nota.codigo, 
                     new_nota.modelo, 
                     new_nota.serie, 
                     #new_nota.tipo_emissao, 
                     constant.DEFAULT_STATUS, 
                     messages.Messages().aguardando_postagem) )
    conn.commit()
    conn.close()

def salva_cnpj_banco(new_nota):
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()
    cursor.execute(constant.QUERY_SAVE_CNPJ,  
                    (
                     new_nota.cnpj, 
                     new_nota.uf, 
                     new_nota.modelo, 
                     new_nota.serie) )
    conn.commit()
    conn.close()   


