import sqlite3
from datetime import datetime

import constant
import messages


def atualiza_status_nota(chave, status):
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_UPDATE_STATUS_NOTA.format(status, chave)
 cursor = conn.cursor()
 cursor.execute(query)
 conn.commit()
 conn.close()

def atualiza_status_message_nota(chave, status, message, cnpj_entidade):
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_UPDATE_STATUS_MESSAGE_NOTA.format(status, message.replace("'",""), datetime.now().strftime('%Y-%m-%d %H:%M:%S'), cnpj_entidade,  chave)
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
 row = cur.fetchone()
 conn.close()
 return row

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
 row = busca_cnpj_padrao()
 if (row):
  cnpj = dict(row)['cnpj']
  return cnpj
 else:
  return constant.EMPTY_STR

def limpa_notas_db():
    conn = sqlite3.connect('notas.db')
    cursor = conn.cursor()

    try:
        cursor.execute(constant.QUERY_DELETA_NOTAS_PROCESSADAS)
        conn.commit()
        conn.close()
    except Exception as err:
        print(repr(err)) 
    finally:
        conn.close()       

def salva_cnpj_padrao_banco(cnpj, descricao, palavras):
 conn = sqlite3.connect('notas.db')
 existe_cnpj = busca_cnpj_padrao_valor()
 query = constant.QUERY_UPDATE_CNPJ_PADRAO if existe_cnpj else constant.QUERY_INSERT_CNPJ_PADRAO
 cursor = conn.cursor()
 query = query.format(cnpj, descricao, palavras )
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

def busca_status_banco():
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_LISTA_STATUS
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 return rows



def busca_chaves_por_status(status, sort = 'ASC'):
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_SELECT_NOTAS_PRINCIPAL_POR_STATUS.format(status, sort)
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 return rows


def busca_uf_banco():
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_LISTA_UF
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

def salva_chave_banco(new_nota, expirada):
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
                     new_nota.tipo_emissao, 
                     constant.DEFAULT_STATUS_CODIGO, 
                     messages.Messages().aguardando_postagem if not expirada else messages.Messages().data_expirada_doacao,
                     datetime.now().strftime('%Y-%m-%d %H:%M:%S') ) )
                   
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


