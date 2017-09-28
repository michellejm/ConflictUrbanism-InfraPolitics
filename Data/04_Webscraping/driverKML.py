#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:28:36 2017

@author: mam
"""

import requests, bs4
from selenium import webdriver

sitelist=[]
subsitelist=[]

url="https://census2011.adrianfrith.com"

outfile = "htmlextensions.txt"

page = requests.get(url+"/place/798")
apage = bs4.BeautifulSoup(page.text)


#Make a list of all the links to the sites within Joburg
for tr in apage.find_all('tr'):
    aref = tr.find_all('a')
    for a in aref:
        sitelist.append(a.get('href'))
    
for site in sitelist[:5]:
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

browser = webdriver.Firefox()
for asite in subsitelist:
    browser.get(url+asite)
    mylink = browser.find_element_by_link_text('download KML file')
    mylink.click()