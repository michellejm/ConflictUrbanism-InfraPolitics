
# coding: utf-8

# In[1]:

import requests, bs4
import pandas as pd
import numpy as np
from collections import defaultdict


# In[2]:

category=['Male', 'Female', 'Black African', 'Coloured', 'Indian or Asian', 'White', 'Sepedi', 'isiZulu', 'Xitsonga', 'Setswana', 'Sesotho', 'isiXhosa', 'Tshivenda', 'English', 'isiNdebele', 'Sign language', 'Afrikaans', 'SiSwati']


# In[3]:

sites=[]
sitelist=[]
subsitelist=[]


# In[4]:

df=pd.DataFrame(columns=category)


# In[5]:

page = requests.get("https://census2011.adrianfrith.com/place/798")
apage = bs4.BeautifulSoup(page.text)


# In[6]:

for tr in apage.find_all('tr'):
    aref = tr.find_all('a')
    for a in aref:
        sitelist.append(a.get('href'))


# In[7]:

print(sitelist)


# In[11]:

for site in sitelist[:5]:
    bpage = requests.get("https://census2011.adrianfrith.com"+site)
    cpage = bs4.BeautifulSoup(bpage.text)
    for tr in cpage.find_all('tr'):
        aref = tr.find_all('a')
        for a in aref:
            subsitelist.append(a.get('href'))

print(subsitelist)


# In[17]:

for subsite in subsitelist[:5]:
    dpage = requests.get("https://census2011.adrianfrith.com"+subsite)
    mypage = bs4.BeautifulSoup(dpage.text)
    
    locats=[]
    elem = mypage.select('.topname')
    locat=elem[0].getText()
    locats.append(locat)
    
    mylist = []
    for tr in mypage.find_all('tr'):
        tds = tr.find_all('td')
        for item in tds:
            mylist.append(item.getText())

    statlist = []
    num = len(mylist)//3
    for n in range(num):
        x = n*3
        y = 1+(n*3)
        statlist.append((mylist[x], mylist[y]))

    mydict = defaultdict(list)
    
    for k,v in statlist:
        if k == "Other":
            pass
        elif k == "Not applicable":
            pass
        else:
            mydict[k].append(v)
            
    df1 = pd.DataFrame.from_dict(mydict, orient='index').transpose()
    se = pd.Series(locats)
    df1['locID'] = se.values
    df=df.append(df1).fillna(value=0)
    


# In[18]:

print(df)


# In[ ]:

df.to_csv('data/jhb_census.csv')


# In[ ]:



