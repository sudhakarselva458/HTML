import mysql.connector
mydb=mysql.connnector.connect(
    host="localhost",
    username="root",
    password="Sudhakar@95",
    database="learning"
)
def insert(name,city,commission):
    mycursor=mydb.cursor()
    sql="insert into salesmen(name,city,commission) values(%S,%S,%S)"
    salesmen=(name,city,commision)
    mycursor.execute(sql,salesmen)
    mycursor.commit()
    print("data inserted successfully")
    #user input
    name=input("Enter name:")
    city=input("Enter city:")
    commission=input("Enter commission")

