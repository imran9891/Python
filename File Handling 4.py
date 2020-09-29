obj = open("sample.text",'w')
obj.write("Welcome to Python Programming")
obj.close()

obj = open("sample.text",'r')
print(obj.read())
obj.close()

import shutil

shutil.copy("sample.text","./File Handling/sample.text")
print('File copied')
shutil.copytree("Test","Best")
print('File copied')
shutil.move("sample.text","Best/sample.text")
print('File Moved')
shutil.rmtree("Test")
print('Folder Removed')

import os

os.rmdir('Test')
print("Folder Removed") # Removes only empty folder

if os.path.exists("sample.text"):
    obj = open("sample.text",'r')
    print(obj.read())
    obj.close()
else:
    obj = open("sample.text",'w')
    obj.write("Welcome to Python Programming")
    obj.close()

os.chdir("Web Server")
for folder,subfolder,file in os.walk(os.getcwd()):
    print(folder)
    print(subfolder)
    print(file)

import send2trash
send2trash.send2trash("Best")
print("Folder Removed")
print(os.getcwd())
print(os.path.exists("Best"))
