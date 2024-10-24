# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 06:05:27 2021

@author: User
"""

dict_1= {"CSCI 115": "Programming Fundamentals", 
           "CSCI 151":"Programming for Scientists and Engineers", 
           "CSCI 152" : "Performance and Data Structures"}
new_dict = {value:key for (key,value) in dict_1.items()}
print(new_dict)
x=input()