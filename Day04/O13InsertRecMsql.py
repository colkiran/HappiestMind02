
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database= "players", port=3306)

cursor = conn.cursor()

# query = "insert into player value ('PL101', 'Mike Tyson', 'USA', '85 KO')"
# query = "insert into player values ('PL240', 'Sachin Tendulkar', 'India', '100 centuries')"
# query = "insert into player values ('PL350', 'Cristiano Ronaldo', 'Portugese', '36 FIFA Worldcup Goals')"
# query = "insert into player values ('PL425', 'Roger Fedrer', 'Switzerland', '20 Grandslams')"
query = "insert into player values ('PL580', 'Tiger Woods', 'USA', '85 PGA Tours')"

cursor.execute(query)

conn.commit()
conn.close()