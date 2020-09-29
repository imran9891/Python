#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Writing CSV File
import csv

with open('./File Handling/employee.csv','w',newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Name','Age','Designation','Salary'])
    writer.writerow(['Aman',28,'Manager',35000])
    writer.writerow(['Saroj',32,'Developer',65000])
    writer.writerow(['Pankaj',26,'Accountant',18000])
    print('Csv File Created')
print("\n")

# Reading CSV File
with open('./File Handling/employee.csv','r') as file2:
    reader = csv.reader(file2)
    
    line_count = 0
    for row in reader:
        # print(row)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works as a {row[2]}, and is now {row[1]} years old.')
            line_count += 1
    print(f'Processed {line_count} lines.')
print("\n")

# Reading CSV with DictReader
with open('./File Handling/employee.csv','r') as file3:
    reader = csv.DictReader(file3)
    
    for row in reader:
        # print(row)
        print(dict(row))
print("\n")

# Writing multiple rows
csv_rowlist = [
    ['Name', 'Age', 'Designation', 'Salary'],
    ['Aman', 28, 'Manager', 35000],
    ['Saroj', 32, 'Developer', 65000],
    ['Pankaj', 26, 'Accountant', 18000]
]

with open('./File Handling/employee2.csv', 'w', newline='') as file4:
    writer = csv.writer(file4)
    
    writer.writerows(csv_rowlist)
    print("Csv File Created")
print("\n")

# Read CSV having comma delimiter
file5 = open('./File Handling/employee.csv','r')
reader = csv.reader(file5)
for row in reader:
    print(row)
print("\n")
with open('./File Handling/employee.csv', 'r') as file5:
    reader  = csv.reader(file5)
    for row in reader:
        print(row)
print("\n")

# Read CSV as a Dictionary
with open('./File Handling/employee.csv', 'r') as file6:
    reader = csv.DictReader(file6)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Col Names are: {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Name"]} works as a {row["Designation"]} and is {row["Age"]} years old.')
        line_count += 1
    print(f'Processed {line_count} lines.') 
print("\n")

# Creating CSV from a Dictionary
with open('./File Handling/employee3.csv', 'w', newline='') as file7:
    fieldnames = ['name','age','depart']
    writer = csv.DictWriter(file7, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'name':'Deepak', 'age':23, 'depart':'IT'})
    writer.writerow({'name':'Saroj', 'age':28, 'depart':'Media'})
    print('Csv file created')

