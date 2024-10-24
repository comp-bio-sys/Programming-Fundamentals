# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:14:40 2021

@author: User
"""

text = "Programming is the process of creating a set of instructions that tell a computer how to perform a task. Programming can be done using a variety of computer programming languages, such as JavaScript, Python, and C++. Different programming languages support different styles of programming. This determines different programming paradigms."
list1 = text.split(". ")
for i in list1:
  if i[0] < 'A' or i[0] > 'P':
    list1.remove(i)
print(list1)