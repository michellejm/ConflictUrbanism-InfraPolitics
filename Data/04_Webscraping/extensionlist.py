#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:44:15 2017

@author: mam
"""
import requests, bs4


mylist = []
sites=[]
sitelist=[]
subsitelist=[]
alist=[]

url="https://census2011.adrianfrith.com"

outfile = "htmlextensions.txt"

page = requests.get(url+"/place/798")
apage = bs4.BeautifulSoup(page.text)


#Make a list of all the links to the sites within Joburg
for tr in apage.find_all('tr'):
    aref = tr.find_all('a')
    for a in aref:
        sitelist.append(a.get('href'))
    
for site in sitelist:
    #Go visit those sites and get the text from them
    bpage = requests.get(url+site)
    cpage = bs4.BeautifulSoup(bpage.text)
    #in that text, search for the tag, 'tr'
    for tr in cpage.find_all('tr'):
        #within the 'tr's, find all the 'a'
        aref = tr.find_all('a')
        #read the href associated with that 'a', and make a list out of it, this will give us a list of links for the subsites
        for a in aref:
            subsitelist.append(a.get('href'))

for subsite in subsitelist:
    myres = requests.get(url+subsite)
    mypage = bs4.BeautifulSoup(myres.text)
    
    elem = mypage.select('.topname')
    loc=elem[0].getText()
    sites.append(loc)
    
    for mc in mypage.select('div > a'):
        mylist.append(mc.get('href'))

    num = len(mylist)//2
    for n in range(num):
        x = 1+ n*2
        alist.append(mylist[x])

with open ('filelist.py', 'w') as f:
    f.write('mylist = %s' % alist)

    
