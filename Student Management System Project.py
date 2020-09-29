print("-------------------------------------------------------")
print("                                                       ")
print("    *****WELCOME TO STUDENT MANAGEMENT SYSTEM*****     ")
print("                                                       ")
print("-------------------------------------------------------")
mydict={}

def wtf(mydict):
              f=open("student.csv","a")
              for k in mydict:
                            line=mydict[k]["name"]+","+mydict[k]["id"]+","+mydict[k]["section"]\
                            +","+mydict[k]["location"]+","+mydict[k]["phone"]+"\n"
                            f.write(line)
                            print(mydict)
              f.close()

def load_file():
              f=open("student.csv","r")
              mydict={}
              for line in f:
                            l=line.split(",")
                            if len(l)==5:
                                          loc_dict={}
                                          loc_dict["name"]=l[0]
                                          loc_dict["id"]=l[1]
                                          loc_dict["section"]=l[2]
                                          loc_dict["location"]=l[3]
                                          loc_dict["phone"]=l[4]
                                          print(loc_dict)
                                          mydict[l[0]]=loc_dict
                                          print(mydict)
              f.close()
              return mydict

def view_slist(mydict):
              for x in mydict:
                            print(mydict[x])

def add_student(name,sid,section,location,phone):
              loc_dict={}
              mydict={}
              loc_dict["name"]=name
              loc_dict["id"]=sid
              loc_dict["section"]=section
              loc_dict["location"]=location
              loc_dict["phone"]=phone
              mydict[name]=loc_dict
              return mydict

def remove(mydict,name):
              f=open("student.csv","r")
              if name in mydict:
                            print(mydict[name])
                            del mydict[name]
                            print("Data removed successfully")
              else:
                            print("Data not found")
              with open("student.csv","w") as f:
                            for k in mydict:
                                          line=mydict[k]["name"]+","+mydict[k]["id"]+","+mydict[k]["section"]\
                                          +","+mydict[k]["location"]+","+mydict[k]["phone"]
                                          f.write(line)
              f.close()
              return mydict

def search(mydict,name):
              f=open("student.csv","r")
              if (name in mydict):
                            print("Record found successfully")
                            print(mydict[name])
              else:
                            print("Record not found")
              f.close()
              return mydict
##wtf(mydict)
def first():
              mydict=load_file()
              while(True):
                            print("Please choose any one options:")
                            print("1. To view student list")
                            print("2. To add new list")
                            print("3. To remove the data")
                            print("4. To search data")
                            print("5: Exit")
                            ch=int(input("Enter your choice: "))
                            if ch==1:
                                          print()
                                          view_slist(mydict)
                                          break
                            elif ch==2:
                                          print()
                                          name=input("Name:")
                                          sid=input("Student_id:")
                                          section=input("Section:")
                                          location=input("Location:")
                                          phone=input("Phone No:")
                                          mydict=add_student(name,sid,section,location,phone)
                                          print("record entered")
                                          wtf(mydict)
                                          break
                            elif ch==3:
                                          print()
                                          name=input("Name:")
                                          mydict=remove(mydict,name)
                            elif ch==4:
                                          print()
                                          name=input("Name:")
                                          search(mydict,name)
                                          break
                            elif ch==5:
                                          print()
                                          exit()

first()
print()
c=input("Want to continue(Y/N): ")
if(c=='y' or c=='Y'):
              first()
else:
              exit()

