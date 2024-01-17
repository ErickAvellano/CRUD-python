import mysql.connector

db_connection = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='erick',
    database ='schooldb'
)

cursor = db_connection.cursor()

select_query = "SELECT * FROM student"

cursor.execute(select_query)

rows = cursor.fetchall()

for row in rows:
    print(row)

db_connection.commit()

cursor.close()
db_connection.close()