import mysql.connector
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Sudhakar@95"


)


#mycursor = mydb.cursor()
#mycursor.execute("create database mydatabase")
mycursor = mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
    print(x)