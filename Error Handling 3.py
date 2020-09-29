'''
Exception Handling in Python
4 types of Blocks:
1. try: run this code
2. except: run this code if an exception occurs
3. else: run this code if no exception occurs
4. finally: always run this code

Exception can be said to be any abnormal condition in a program resulting to
the disruption in the flow of program. Whenever an exception occurs the program
halts the execution and thus further code is not executed.

Various types of errors on different situations:

1. Zero Division Error: It occurs when a no. is divided by zero.
for i in range(-5,5):
print(100/i)

2. Name Error: It occurs when a name is not found. It may be local or global.
var=5
print(ver)

3. Syntax Error:
print('Hello)

4. Type Error:
x=5+'aman'
print(x)

5. Index Error:
mylist=[1,2,3]
print(mylist[4])

6. Key Error:
mydict={'a':1,'b':2,'c':3,'d':4}
key=input('Plz input a key')
print('The value for {0} is {1}'.format(key,mydict[key]))

7. Value Error: factorial() not defined for negative values.
import math
num=int(input("Enter any no."))
result=math.factorial(num)
print(result)

8.Indentation Error: If incorrect indentation is given.
age=int(input('Enter your age:'))
if(age>=18):
print('U are eligible for voting')

9.IO Error: Raised when an input/output operation fails, such as the open() function when trying to open a file
that does not exists.
obj=open('sample.text','r')
s1=obj.read()
print(s1)
obj.close()
'''

# Using pass continue, handle zero division error:

for i in range(-5,6):
    print(100/i)
              
for i in range(-5,6):
    try:
        x = 100/i
        print(x)
    except ZeroDivisionError:
        continue

r_list=[]
e_list=[]
for i in range(-5,6):
    try:
        x = 100/i
        print(x)
    except ZeroDivisionError as Err:
        e_list.append('Answer: ' +str(Err))
    else:
        r_list.append('Answer: ' +str(x))
print(e_list)
print(r_list)

# Used Exception Keyword is father of all errors and this is used when error is unidentified

r_list=[]
e_list=[]
for i in range(-5,6):
    try:
        x=100/i
        print(x)
    except Exception as Err:
        e_list.append('Answer ' + str(Err))
    else:
        r_list.append('Answer ' + str(x))
print(e_list)
print(r_list)

# User Defined Exception by assert keyword
# assert(): a predefined method, used for creating user defined exception.

def f2k(temp):
             assert(temp>0),'Temperature is so cold'
             return((273-temp)*2)
print(f2k(273))

# raise(): This keyword is used for raising the error explicitly
# raise TypeError("This is raising the error")

# Name Error

try:
    a=10
    print(a)
    raise NameError ("Hello")
except NameError as e:
    print("An exception occured")
    print(e)

# Raise Value Error

try:
    num=int(input("Enter any no."))
    if num<=0:
        raise ValueError("That is not positive number")
except ValueError as error:
             print(error)
print(num)

import math
num=int(input("Enter the no. "))
try:
    result=math.factorial(num)
    print(result)
except ValueError:
    print('Cant compute the factorial of negative numbers')

# Key Error

mydict={'a':1,'b':2,'c':3,'d':4}
key=input('Please input a key: ')
try:
    print("Testing for Error")
    print('The value for {0} is {1}'.format(key,mydict[key]))
except KeyError:
    print('Trapped Error')
    print("This Key " + key + " does not exist")

# Finally Block

import math
num=int(input('Enter any number: '))
try:
    result=math.factorial(num)
    print(result)
finally:
    print('Best Wishes')

# I/o Error

try:
    obj=open('sample.txt','r')
    obj.write('This is my test file for exception handling!!')
except IOError:
    print('Error! Can\'t find file or read data')
else:
    print('Written content in the file successfully')
    obj.close()

# Type Error:
try:
    x=5 + 'aman'
except TypeError:
    print('Integer and string value can\'t be added')
