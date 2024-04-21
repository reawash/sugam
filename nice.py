'''import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "customers"
)
mycursor=mydb.cursor()'''
'''mycursor.execute("Create Database Customers")
print("Database created sucessfully")'''

"""mycursor.execute("Create table cus_table(name varchar(110), age varchar(2),address varchar(120),cont_per varchar(120))")
print("Data table created sucessfully")
 """

"""sql="insert into cus_table(name,age,address,cont_per)values(%s,%s,%s,%s,%s)"
val=("Mr Dhoni","44","Ranchi","Mr Dewan")
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")
"""
'''sql="insert into the table"

mycursor.executenary()
mydb.commit()
print(mycursor.rowcount,"has inserted")

sql="select*from cus_table where name ='mrs.dey'"
'''

#Employee management:-
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "Emp_Man"
)
mycursor=mydb.cursor()
'''mycursor.execute("Create database Emp_Man")
print("Database created sucessfully")
'''
'''mycursor.execute("Create table emp_table(id int(2) primary key auto_increment,name varchar(120),address varchar(120),phone varchar(10),mail varchar(100),department varchar(100))")
print("Table created sucessfully")

'''
'''sql="insert into emp_table(id,name,address,phone,mail,department)values(%s,%s,%s,%s,%s,%s)"
val=[
    ('',"Mr Das","Kolkata","9786535279","das@gmail.com","sales"),
    ('',"Mrs Adhikari","Darjeeling","9734629173","adhikari@gmail.com","accounts"),
    ('',"Mr.sam","Kurseong","9745628362","sam","purchase",)
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"row/s inserted")

'''
'''sql="select*from emp_table"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for u in myresult:
    print(u)
'''
sql="update emp_table set name=%s where name=%s"
val=("Mrs.Das","Mr.Das")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"row/s affected")


