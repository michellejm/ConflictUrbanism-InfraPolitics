#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:21:31 2017

@author: mam
"""

import urllib.request

url="https://census2011.adrianfrith.com"

from listfile import mylist as mylist

links = []
for i in mylist:
    links.append(url+i)
    
for link in links:
    n=str(links.index(link))    
    urllib.request.urlretrieve(link, "kmls/file"+n+"2.kml")

    

    
