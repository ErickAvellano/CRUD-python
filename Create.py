import mysql.connector

db_connection = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='erick',
    database ='schooldb'
)

cursor = db_connection.cursor()

data_to_insert = [("1","Erick","Avellano","09154067307"),
                ("2","Alexis","Llena","09123456789")]

insert_query = "INSERT INTO student(id, firstname, lastname, contact) VALUES (%s, %s,%s,%s)"

cursor.executemany(insert_query,data_to_insert)

db_connection.commit()

cursor.close()
db_connection.close()

