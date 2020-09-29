#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res)
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')

# print(soup.title)
# print(soup.body)
# print(soup.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.a)
# print(soup.find(id="score_24543121"))
# print(soup.select('a'))
# print(soup.select('.score'))
# print(soup.select('#score_24543121'))
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
mega_links = links + links2
mega_subtexts = subtext + subtext2
# print(links[0])
# print("\n")
# print(subtext[0])
# print("\n")

def create_custom_hn(links, subtext):
    li = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        vote = subtext[idx].select('.score')
        if vote:
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                li.append({'Title': title, 'Link': href, 'Points': points})
                a = sorted(li,key=(lambda key:key['Points']),reverse=True)
    return a

pprint.pprint(create_custom_hn(mega_links, mega_subtexts),indent=3,width=80)

