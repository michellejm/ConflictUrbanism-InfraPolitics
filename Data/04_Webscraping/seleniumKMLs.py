#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:21:31 2017

@author: mam
"""

import requests, bs4
import urllib.request


url="https://census2011.adrianfrith.com"
#page = requests.get(url+"/place/798")
#apage = bs4.BeautifulSoup(page.text)

from listfile import mylist as mylist

links = []
for i in mylist[274:]:
    links.append(url+i)
    
for link in links:
    n=str(links.index(link))    
    urllib.request.urlretrieve(link, "kmls/file"+n+"2.kml")

    

    