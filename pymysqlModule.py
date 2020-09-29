#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Connect Mysql database & create new database & open Xammp

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='')
a = conn.cursor()
a.execute('CREATE DATABASE demo')
print('Demo database created')
print("\n")

# Create Table of selected Database

conn = pymysql.connect(host='localhost', user='root', password='', db='demo')
a = conn.cursor()

a.execute('''
CREATE TABLE COMPANY
(ID      INT PRIMARY KEY NOT NULL,
 NAME    TEXT NOT NULL,
 AGE     INT NOT NULL,
 ADDRESS CHAR(50),
 SALARY  REAL)''')
print('Table created successfully')
conn.close()
print("\n")

# Inserting Records into the table

conn = pymysql.connect(host='localhost', user='root', password='', db='demo')
a = conn.cursor()

a.execute("INSERT INTO COMPANY VALUES (1, 'Paul', 32, 'California', 20000.00)")
a.execute("INSERT INTO COMPANY VALUES (2, 'Sam', 31, 'Bahamas', 40000.00)")
a.execute("INSERT INTO COMPANY VALUES (3, 'Dean', 35, 'Corsica', 10000.00)")
a.execute("INSERT INTO COMPANY VALUES (4, 'Lucy', 36, 'Amazon', 90000.00)")
a.execute("INSERT INTO COMPANY VALUES (5, 'John', 37, 'Mars', 22000.00)")
a.execute("INSERT INTO COMPANY VALUES (6, 'Gerard', 22, 'Texas', 30000.00)")
print("Records Inserted...")
conn.commit()
conn.close()
print("\n")

# Display all Records

conn = pymysql.connect(host='localhost',user='root',password='',db='demo')
a = conn.cursor()
a.execute("SELECT * FROM COMPANY")
data = a.fetchall()
for row in data:
    print("ID=", row[0])
    print("NAME=", row[1])
    print("AGE=", row[2])
    print("ADDRESS=", row[3])
    print("SALARY=", row[4],"\n")
print("Operation done successfully")
conn.close()
print("\n")

# Update Records

conn = pymysql.connect(host='localhost',user='root',password='',db='demo')
a = conn.cursor()

a.execute("UPDATE COMPANY SET SALARY=5000.00 WHERE ID=1")
a.execute("UPDATE COMPANY SET NAME='Lucious' WHERE ID=2")
conn.commit()

a.execute("SELECT ID, NAME, ADDRESS, SALARY FROM COMPANY")
data = a.fetchall()
for row in data:
    print("ID=", row[0])
    print("NAME=", row[1])
    print("ADDRESS=", row[2])
    print("SALARY=", row[3],"\n")
print("Operation done successfully")
conn.close()
print("\n")

# Delete Records

conn = pymysql.connect(host='localhost',user='root',password='',db='demo')
a = conn.cursor()

a.execute("DELETE FROM COMPANY WHERE ID=3")
conn.commit()

a.execute("SELECT ID, NAME, ADDRESS, SALARY FROM COMPANY")
data = a.fetchall()
for row in data:
    print("ID=", row[0])
    print("NAME=", row[1])
    print("ADDRESS=", row[2])
    print("SALARY=", row[3],"\n")
print("Operation done successfully")
conn.close()
print("\n")

# Drop Complete Database

conn = pymysql.connect(host='localhost', user='root', password='', db='demo')
a = conn.cursor()

a.execute("DROP DATABASE demo")
conn.commit()

a.execute("SELECT * FROM COMPANY")
data = a.fetchall()
for row in data:
    print("ID=", row[0])
    print("NAME=", row[1])
    print("ADDRESS=", row[3])
    print("SALARY=", row[4],"\n")
print("Database Deleted Forever")
conn.close()
print("\n") 

