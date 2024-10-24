# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:07:59 2021

@author: User
"""

l= [10, 15, -12, 24, 17, -6, 6, 18]
l1=[]
for i in l:
  if(i>0 and (i%3==0 or i%5==0 or i%7==0)):
     l1.append(i)
d=l1[::-1]
print(d)