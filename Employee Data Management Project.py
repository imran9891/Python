print("--------------------------------------------------------------")
print("    Employee Data Management System    ")
print("--------------------------------------------------------------")

##import os,sys


mydict={}

def load_data():
        f=open("employee.csv", "r")
        mydict={}
        for line in f:
                l=line.split(",")
                if len(l)==5:
                        local_dict={}
                        local_dict["name"]=l[0]
                        local_dict["employee_id"]=l[1]
                        local_dict["department"]=l[2]
                        local_dict["title"]=l[3]
                        local_dict["salary"]=l[4]
                        print(local_dict)
                        mydict[l[0]]=local_dict
                        print(mydict)
        f.close()
        return mydict

def display_data(mydict):
        for k in mydict:
                print(mydict[k])


def add_employee(name, employee_id, department, title, salary):
        local_dict={}
        mydict={}
        local_dict["name"]=name
        local_dict["employee_id"]=employee_id
        local_dict["department"]=department
        local_dict["title"]=title
        local_dict["salary"]=salary
        mydict[name]=local_dict
        return mydict


def find_by_id(mydict, id):
        flag=0
        for k in mydict:
                d=mydict[k]
                if d["employee_id"]==id:
                        flag=1
                        print("record found")
                        print(d)
                
             
        if flag==0:
                 print("record not found")

def find_by_name(mydict, name):
        flag=0
        for k in mydict:
                d=mydict[k]
               # print(d)
                if d["name"]==name:
                        flag=1
                        print("record found")
                        print(d)
        if(flag==0):
                print("record not found")
	

def delete_employee(mydict, name):
        f=open("employee.csv","r")
        if(name in mydict):
                print(mydict[name])
                del mydict[name]
                print(" record deleted")
        else:
                print("record not found")
        with open("employee.csv","w") as f:      
                for k in mydict:
                           line=mydict[k]["name"]+","+mydict[k]["employee_id"]+","+mydict[k]["department"]\
                           +","+mydict[k]["title"]+","+mydict[k]["salary"]
                           f.write(line)
        f.close()
        return mydict


def write_to_file(mydict):
              f=open("employee.csv", "a")
              for k in mydict:
                   line=mydict[k]["name"]+","+mydict[k]["employee_id"]+","+mydict[k]["department"]\
                  +","+mydict[k]["title"]+","+mydict[k]["salary"]+"\n"
                   f.write(line)
              f.close()


##write_to_file(mydict)
def first():
     mydict=load_data()
     while True:
            print("1. Add an Employee")
            print("2. Find an Employee (By Name)")
            print("3. Find an Employee (By EID)")
            print("4. Delete an Employee")
            print("5. Display Statistics")
            print("6. Exit")
            choice=int(input("Enter the choice:"))
            if(choice==1):
                    name=input("name:")
                    employee_id=input("employee_id:")
                    department=input("department:")
                    title=input("title:")
                    salary=input("salary:")
                    mydict=add_employee(name, employee_id, department, title, salary)
                    print("record entered")
                    write_to_file(mydict)
                    break
            elif(choice==2):
                    name=input("name:")
                    find_by_name(mydict, name)
            elif(choice==3):
                   id=input("id:")
                   find_by_id(mydict, id)
            elif(choice==4):
                   name=input("name")
                   mydict=delete_employee(mydict, name)
            elif(choice==5):
                  display_data(mydict)     
first()
a=input("enter y if u want to continue otherwise n :")
if(a=='y'):
        first()
else:
        exit()


