# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:12:23 2021

@author: User
"""

a,b,c=0,0,""
password=input("password = ")
for i in password:
    if(i.isupper()):
        a+=1
    if(i.isdigit()):
        b+=1
if(a>=1 and b>=2 and len(password)>=8):
    print("The password is valid")
if len(password)<8:
    c+= "The given password is too short,"
if(b<2):
    c+= "digits condition is broken,"
if(a<1):
    c+="no uppercase symbol was given,"
print(c.rstrip(","))