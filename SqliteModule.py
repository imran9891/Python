#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create & Connect Database
import sqlite3 as db

conn = db.connect('./SQL/demo.db')
print("Database created successfully")
print("\n")

# How to connect demo database & create table & close the connection
# If you want to write any db query in multiple lines then you can use triple quotes otherwise 
# if you write in single line then use single or double quotes.

conn = db.connect('./SQL/demo.db')
print('Database Connected')
conn.execute('''CREATE TABLE COMPANY
(ID        INT     PRIMARY KEY NOT NULL,
 NAME      TEXT    NOT NULL,
 AGE       INT     NOT NULL,
 ADDRESS   CHR(50),
 SALARY    REAL)''')
print("Table Created Successfully")
conn.close()
print("\n")

# Inserting Multiple Records in a Table

conn = db.connect('./SQL/demo.db')

conn.execute("INSERT INTO COMPANY VALUES (1, 'Paul', 32, 'California', 20000.00)")
conn.execute("INSERT INTO COMPANY VALUES (2, 'Sam', 31, 'Bahamas', 40000.00)")
conn.execute("INSERT INTO COMPANY VALUES (3, 'Dean', 35, 'Corsica', 10000.00)")
conn.execute("INSERT INTO COMPANY VALUES (4, 'Lucy', 36, 'Amazon', 90000.00)")
conn.execute("INSERT INTO COMPANY VALUES (5, 'John', 37, 'Mars', 22000.00)")
conn.execute("INSERT INTO COMPANY VALUES (6, 'Gerard', 22, 'Texas', 30000.00)")

conn.commit()
print('Records Inserted...')
conn.close()
print("\n")

# Display all records of selected Table

conn = db.connect('./SQL/demo.db')
cursor = conn.execute("SELECT * FROM COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4],"\n")
    
print("Operation done successfully")
conn.close()
print("\n")

# Update Records of Selected Table

conn = db.connect('./SQL/demo.db')
conn.execute("UPDATE COMPANY set SALARY = 5000.00 WHERE ID=1")
conn.execute("UPDATE COMPANY SET NAME = 'LUCIOUS' WHERE ID=2")
print("Total no. of rows updated :",conn.total_changes)
conn.commit()
cursor = conn.execute("SELECT ID,NAME,ADDRESS,SALARY FROM COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3],"\n")
    
print("Operation Done Successfully")
conn.close()
print("\n")

# Delete Records from selected Table

conn = db.connect('./SQL/demo.db')
conn.execute("DELETE FROM COMPANY WHERE ID=3")
print("Total no. of row deleted", conn.total_changes)
conn.commit()

cursor = conn.execute("SELECT * FROM COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4],"\n")

print("Operartion done successfully")
conn.close()
print("\n")

# Drop Full Table

conn=db.connect('./SQL/demo.db')
conn.execute("DROP TABLE COMPANY")
conn.commit()
cursor=conn.execute("SELECT * FROM COMPANY")    #shows error in fetching
for row in cursor:
             print("ID=",row[0])
             print("NAME=",row[1])
             print("AGE=",row[2])
             print("ADDRESS=",row[3])
             print("SALARY=",row[4],"\n")
print("Operation done successfully")
conn.close()

