import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost" ,
    port = 3306 ,
    user = "root" ,
    password = "root" ,
    database = "PYTHON_SQL"
)

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE PYTHON_SQL")

# print("Data - Base Created Successfully!!")

# CREATE TABLE --------------------------

"""
cursor.execute('''            
                CREATE TABLE IF NOT EXISTS student (
                    id INT AUTO_INCREMENT PRIMARY KEY ,
                    name VARCHAR(50) ,
                    salary INT ,
                    mobileNo VARCHAR(10) ,
                    marks INT
                                                    )
            ''')

print("\nTable Created Successfully!!")

"""

# INSERT QUERY --------------------------

# cursor.execute("INSERT INTO student (name, salary , mobileNo , marks) VALUES ('Chirag', 15000 , 9856369874 , 99)")

# cursor.execute("INSERT INTO student (name, salary , mobileNo , marks) VALUES ('Suresh', 25000 , 9656369874 , 90)")

# cursor.execute("INSERT INTO student (name, salary , mobileNo , marks) VALUES ('Ramesh', 50000 , 9256369874 , 94)")

# mydb.commit()

# print("\nData Inserted Successfully!!")

# UPDATE QUERY --------------------------

# cursor.execute("UPDATE student SET salary = 6000 WHERE id = 3")

# mydb.commit()

# print("\nThe Data Updated Successfully!!")

# DELETE QUERY --------------------------

# cursor.execute("DELETE FROM student WHERE id = 2")

# mydb.commit()

# print("\nThe Data can be Deleted Successfully!!")

# FETCHING ALL THE DATA HERE ---------------------

cursor.execute("SELECT * FROM student;")

rows = cursor.fetchall()

for i in rows :
    print(i)

cursor.close()

mydb.close()