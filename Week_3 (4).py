# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:30:19 2021

@author: User
"""

countries=['Ecuador','USA','Ghana','Germany','Armenia','Cuba','Norway']     
areas=[248360,9147420,227540,348560,28470,106440,365268]
l=[]
for i in countries:  
     if((('z' not in i) and ('k' not in i) and ('t' not in i) and ('u' not in i))and((len(i)%2)==0)):
        l.append(i)
        l1=[]
        for i in l:
            for k in countries:           
              for j in areas:
                  if(i==k):             
                    if(countries.index(k)==areas.index(j)):
                     l1.append(j)
                     for i in l1:
                      for j in l:
                        if(l1.index(max(l1))==l.index(j)):
                         c=j           

print("The largest country in the list that satisfy conditions is "+c+" with the area of "+str(max(l1)))
                  