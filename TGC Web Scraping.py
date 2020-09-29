#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://www.tgcindia.com/blog/')
res2 = requests.get('https://www.tgcindia.com/blog/page/2/')
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')
soup.prettify
# print(soup.title)
twl = soup.select('h3')
twl2 = soup.select('h3')
megatwl = twl + twl2

def get_blogs(body):
    li = []
    for idx, item in enumerate(body): 
        title = item.getText()
        link = item.select('a')
        hlink = link[0].get('href',None)
        li.append({'Title': title,
                   'Link': hlink})
    with open ('./Web Scraping/TGC.doc',mode='w') as file:
        file.write(str(li))
        
    return li
        
pprint.pprint(get_blogs(megatwl),indent=3, width=90)

