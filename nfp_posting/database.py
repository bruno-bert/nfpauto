import sqlite3
import constant

def busca_steps(script_id):
 conn = sqlite3.connect('notas.db')
 query = constant.QUERY_SELECT_STEPS.format(script_id)
 conn.row_factory = sqlite3.Row
 cur = conn.cursor()
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 return rows

