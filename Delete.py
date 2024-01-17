import mysql.connector

db_connection = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='erick',
    database ='schooldb'
)

cursor = db_connection.cursor()

data_to_delete = ("1",)

delete_query = "DELETE FROM student WHERE id = %s"

cursor.execute(delete_query,data_to_delete)

db_connection.commit()

cursor.close()
db_connection.close()
