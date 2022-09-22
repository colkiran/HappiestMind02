
import pymysql
from prettytable import PrettyTable, from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database= "players", port=3306)

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)
plyrTbl = from_db_cursor(cursor)

# for row in cursor.fetchall():
#     print(row)

conn.close()

plyrTbl.align['plyname'] = 'l'
plyrTbl.align['sport'] = 'l'
plyrTbl.align['acheievement'] = 'l'

print(plyrTbl)