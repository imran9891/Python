#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Regular Expression in Python:

import re (Built-in Module)
1. re.match()
2. re.search()
3. re.sub()
4. re.find()
5. re.findall()
6. re.compile()
7. re.split()

str="Welcome"
str="/^[A-Z][a-z][0-9]*$/" *: may be not or may be 1 time or may be more time
str="/^(0-9){3,7}$/"

A regular expression is a special sequence of characters that helps you match
or find other strings or sets of strings using a specialized syntax held in a
pattern.

match(): it always match at starting string position and do not match at the
middle or the end of the string.
syntax: re.match(pattern,string,flags=0)
groups(): This method returns all matching subgroups in a tuple (empty if there
weren't any.

'''

import re
def main():
    line="i think that i understand the reg ex"
    match_result=re.match(r'I think',line,re.M|re.I)
    #match_result=re.match(r'think',line,re.M|re.I)
    if match_result:
        print("Match found: " + match_result.group())
    else:
        print("No Match found")
main()


'''
search(): This function searches for first occurence of RE pattern within string with optional
flags. syntax: re.search(pattern,stri\ng,flags=0) match checks for a match only at the beginning
of the string while search checks for a match anywhere in the string.

'''

def main():
    line="i think that i understand the reg ex"
    search_result=re.search(r'Think',line,re.M|re.I)
    if search_result:
        print("Search found: " +search_result.group())
    else:
        print("Search not found")
main()

'''
Search, Replace and Remove using sub() function: This method replaces all occurences of the RE
pattern in string with repl, substituting all occurences unless max provided. This method returns
modified string. syntax: re.sub(pattern,repl,string)

'''

phone = "2004-959-559 # This is Phone Number"
num = re.sub(r'#.*',"",phone)
print("Phone Num : ",num)
num=re.sub(r'#.*',"give anything",phone)
print("Phone Num : ",num)
# Replaces digits with empty blank
num = re.sub(r'\d',"",phone)
print("Phone Num : ",num)
# Removes anything other than digits
num = re.sub(r'\D',"#",phone)
print("Phone Num : ",num)


# findall()

teststring="Captain is avenger the first avenger"
word=re.findall('avenger',teststring)
print(word)
print(word[0])
print(word[1])

string='''
mikaelson are owners of new orleans. the furious one is Niklaus which is 1000 years old and the
nobel one is Elijah which is also 999 years old and there dear sister Rebakha which is 888 years
old.
'''
ages=re.findall(r'\d{1,4}',string)
names=re.findall(r'[A-Z][a-z]*',string)
print(ages)
print(names)
namedict={}
x=0
for n in names:
    namedict[n]=ages[x]
    x+=1
print(namedict)

# Split():

string1="This is My First Web Page, It is using CSS, HTML & Bootstrap"
print(re.split(r'\s',string1))
print('\n')
print(re.split(r's',string1))
print('\n')
print(re.split(r',',string1))

# 1          
print('\n')
def space(str1):
    return(re.sub(r'(\w)([A-Z])',r'\1 \2',str1))
print(space("WelcomeToPythonProgramming"))

# 2
print('\n')
para='''Most people infected with the COVID-19 shallosharma0423@gmail.com virus will experience mild to moderate
respiratory illness and recover babitamehta88@gmail.com without requiring special treatment. Older people, and
those with underlying medical problems like cardiovascular gootyhaindhavi999@gmail.com disease, diabetes, chronic
respiratory disease, and cancer are more likely to develop mdzafarahmed210293@gmail.com serious illness. The best way to
tahirneyaz@gmail.com prevent and slow down transmission is vishalksingh905@gmail.com be well informed about the COVID-19
virus, the sharma.krishna455@gmail.com disease it causes and how akshansh01haldiya@gmail.com it spreads. Protect
yourself and others from infection by osikasonboir@gmail.com washing your hands or using an alcohol based rub
koolkkrishnaa@gmail.com frequently and not touching your face.The COVID-19 virus spreads primarily through droplets
of saliva or discharge sarfraj.ahmedcz3@gmail.com from the nose when an infected person coughs or sneezes, so it’s
important that you also practice respiratory etiquette vyas.abhishiek@gmail.com (for example, by coughing into a flexed
elbow). At this time, there are no specific vaccines or treatments hira.shazi@gmail.com for COVID-19. However, there are
many ongoing clinical trials evaluating potential treatments. WHO will continue kskdina36@gmail.com to provide updated
information as soon as clinical findings become available.'''
print(re.findall(r'\S+@\S+',para))

# 3
print('\n')
print('Password Checker')
while True:
    password=input('Enter the password: ')
    x=print(re.match(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@&_]).{7})',password))
    if x:
        print(res.group())
        print("Password satisfied")
    else:
        print("Not Satisfied")

