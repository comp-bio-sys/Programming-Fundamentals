# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 22:31:41 2021

@author: User
"""

colors = ['#C2345C', '#B71243', '#76121A' , '#C2345C' , '#76121A' , '#76121A']
dic={}
value= set(colors)
for i in colors:
    if i in dic.keys():
        dic[i] = 1 + dic[i]
    else:
        dic[i] = 1
print (dic) 

for w in sorted(dic, key = dic.get):
    print("Color", w,"appear", dic[w], "times in the list")