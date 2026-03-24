import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root"
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE 25GEN_PYTHON")

print("Database created successfully")

cursor.close()

mydb.close()