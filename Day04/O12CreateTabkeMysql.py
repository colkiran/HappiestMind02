import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database= "players", port=3306)

cursor = conn.cursor()

query = """
create tavble player (
plyid varchar(5) PRIMARY KEY,
plyname varchar(50) Not Null,
sport varchar(50) Not Null,
achievement varchar(50) Not Null
)
"""
cursor.execute(query)

conn.close()
