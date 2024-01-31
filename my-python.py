

from tabulate import tabulate
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Sudhakar@95",
    database="learning"
)
def insert(id,name,city,commission):
    con=mydb.cursor()
    sql="insert into table salesmen(id,name,city,commission)  values(%S,%S,%S,%S)"
    salesmen=(id,name,city,commission)
    con.execute(sql,salesmen)
    con.commit()
    print("data inserted successfully")

def update(id,name,city,commission):
    con=mydb.cursor()
    sql="update salesmen set id=%S name=%S,city=%S,commission=%S where id=%S"
    salesmen=(id,name,city,commission)
    cn.execute(sql,salesmen)
    con.commit()
    print("data updated successfully")
def select():
    con=mydb.cursor()
    sql="select * from salesmen"
    con.execute(sql)
    result=con.fetchall()
    #print(result)
    print(tabulate(result,headers=["id","name","city","commission"]))
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
        id=input("Enter id:")
        name=input("Enter name:")
        city=input("Enter city:")
        commission=input("Enter commission:")
        insert(id,name,city,commission)
    elif choice==2:
        id=input("Enter id:")
        name=input("Enter name:")
        city=input("Enter city:")
        commission=input("Enter commission:")
        update(id,name,city,commission)
    elif choice==3:
        select()
    elif choice==4:
        delete()
    elif choice==5:
        quit()
    else:
        print("details entered invalid")
