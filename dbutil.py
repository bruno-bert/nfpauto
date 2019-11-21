import sqlite3

def execute_sql(sql):
 conn = sqlite3.connect('notas.db') 
 cursor = conn.cursor()
 cursor.execute(sql)
 conn.commit()
 conn.close()
