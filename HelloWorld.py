import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
username="root",
password="Sudhakar@95",
database="mydatabase"
)

"""for database
mycursor=mydb.cursor()
mycursor.execute("show databases")
for x in mycursor:
   print(x)
mycursor=mydb.cursor()
mycursor.execute("create table student(id int,name varchar(50),marks int)")
mycursor=mydb.cursor()
mycursor.execute("show tables")
for x in mycursor:
    print(x)"""
