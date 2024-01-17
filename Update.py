import mysql.connector

db_connection = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='erick',
    database ='schooldb'
)

cursor = db_connection.cursor()

data_to_update = ("Albert","Avellano","09154067307","1")

update_query = "UPDATE student SET firstname = %s, lastname = %s, contact = %s WHERE id = %s"

cursor.execute(update_query,data_to_update)

db_connection.commit()

cursor.close()
db_connection.close()

