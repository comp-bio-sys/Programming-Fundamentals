# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 06:22:40 2021

@author: User
"""
animals = {'African Grey Parrot':50, 'Box Turtle':123, 'Chicken':18, 'Deer':35, 'Elephant': 70, 'Rhinoceros':40} 
d=list(animals.values()) 
average= sum(d)/len(animals)
print("The average lifespan of the animal species is", average)
new_list=[]
for key, value in animals.items():
    if value < average :
        pass
    else:
       new_list.append(key) 
print('The list of animals that have above average lifespan is :',new_list)