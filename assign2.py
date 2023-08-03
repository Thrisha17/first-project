import mysql.connector
from tabulate import tabulate


conn = mysql.connector.connect(host='localhost', password='Niranjana#6', user='root', database='python_db')


def insert(name, age, city):

    res = conn.cursor()
    sql = "insert into users (name,age,city) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql, user)
    conn.commit()
    print("Data inserted successfully")


def bulk_insert(records):
    res = conn.cursor()
    sql = "INSERT INTO users(name,age,city) VALUES(%s,%s,%s)"
    res.executemany(sql, records)
    conn.commit()
    print("Bulk insert successful")


def update(name, age, city, id):
    res = conn.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city, id)
    res.execute(sql, user)
    conn.commit()
    print("Data updated successfully")


def select():
    res = conn.cursor()
    sql = "SELECT ID,NAME,AGE,CITY from users"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID,NAME,AGE,CITY "]))


def delete(id):
    res = conn.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    conn.commit()
    print("Data deleted successfully")


while True:

    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Bulk insert")
    print("6.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        name = input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")
        insert(name, age, city)
    elif choice == 2:
        id = input("Enter id : ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")
        update(name, age, city, id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter id:")
        delete(id)
    elif choice == 5:
        records = []
        num_records = int(input("Enter the no of records : "))
        for i in range(num_records):
            name = input("Enter  name:")
            age = int(input("Enter age: "))
            city = input("Enter  city: ")
            records.append((name, age, city))
            bulk_insert(records)
    elif choice == 6:
        quit()
    else:
        print("Invalid selection")



