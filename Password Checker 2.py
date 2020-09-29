#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import hashlib

def access_api(char):
    url = 'https://api.pwnedpasswords.com/range/' + char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error in fetching: {res.status_code}, check the api & try again')
    return res

def password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,c in hashes:
        if h == hash_to_check:
            return c
    return 0
       
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    print(first5, tail)
    response = access_api(first5)
    print(response)
    return password_leaks_count(response, tail)

with open('./Password Checker/pass.txt','r') as file:
        pwd = file.read()
        pwd_li = pwd.split("\n")

def main(pwd_list):
    for item in pwd_list:
        count = pwned_api_check(item)
        if count:
            print(f'{item} has been pwned {count} times. Better to change password')
            print("\n")
        else:
            print(f'{item} has not been pwned. Kudos!')
            print("\n")
    return 'done'

if __name__ == '__main__':
    print(main(pwd_li))

