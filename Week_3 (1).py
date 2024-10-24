# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:00:31 2021

@author: User
"""

def isPalindrome(s):
 return s == s[::-1]  
s= input()
a= list(s.split(" "))
turn = 0
for i in a:
 if isPalindrome(i):
  if turn == 0:
   print("Alice chooses", i)
 turn = 1
else:
 print("Bob chooses", i)
turn = 0
if turn == 0:
 print("Noooo, Alice has lost!")
else:
 print("Noooo, Bob has lost!")