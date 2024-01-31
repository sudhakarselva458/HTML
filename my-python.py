

from tabulate import tabulate
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Sudhakar@95",
    database="learning"
)
def insert(name,city,commission):
    con=mydb.cursor()
    sql="insert into table salesmen(name,city,commission)  values(%S,%S,%S)"
    salesmen=(name,city,commission)
    con.execute(sql,salesmen)
    con.commit()
    print("data inserted successfully")

def update(name,city,commission):
    con=mydb.cursor()
    sql="update salesmen set name=%S,city=%S,commission=%S"
    salesmen=(name,city,commission)
    cn.execute(sql,salesmen)
    con.commit()
    print("data updated successfully")
def select():
    con=mydb.cursor()
    sql="select * from salesmen"
    con.execute(sql)
    result=con.fetchall()
    #print(result)
    print(tabulate(result,header=["id","name","city","commission"]))
def delete(id):
    con=mydb.cursor()
    sql="delete from salesmen where id=%S"
    salesmen=(id,)
    con.execute(sql,salemen)
    print("data deleted successully")

while True:
    print("1.insert")
    print("2.upadte")
    print("3.select")
    print("4.delete")
    print("5.Exit")
    choice=int(input("select the action:"))
    if choice==1:
        name=input("Enter name:")
        city=input("Enter city:")
        grade=input("Enter commission:")
        insert(name,city,commission)
    elif choice==2:
        id=input("Enter id:")
        name=input("Enter name:")
        city=input("Enter city:")
        grade=input("Enter commission:")
        update(name,city,commission)
    elif choice==3:
        select()
    elif choice==4:
        delete()
    elif choice==5:
        quit()
    else:
        print("details entered invalid")
