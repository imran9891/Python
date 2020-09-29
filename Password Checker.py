#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests                  # For accessing url
import hashlib                   # For SHA1 Hashing

def access_api(char):
    url = 'https://api.pwnedpasswords.com/range/' + char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error in fetching: {res.status_code}, check the api & try again')
    return res



def get_password_leaks_count(hashes, hash_to_check):
    # print(hashes.text.splitlines())
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,c in hashes:
        # print(h,c)
        if h == hash_to_check:
            print(h)
            return c
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    print(first5, tail)
    response = access_api(first5)
    print(response)
    return get_password_leaks_count(response, tail)


def main(*args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. It\'s time you should change your password')
            print("\n")
        else:
            print(f'{password} was not pwned.')
            print("\n")
    return 'done'


print(main('123Hello','Imran','Manish'))

