# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:30:41 2021

@author: User
"""

with open(r'C:/Users/User/Desktop/DIC(A).txt', 'r') as f:  
        lines = f.readlines()  

dict_ = dict()
for line in lines: 
        data =(line.split(" ", 1))
        key = data[0].strip().lower() 
        value = (data[1:]) 
        dict_[key] = " ".join(value)  

words = [] 
while True: 
        a = input('\nInput word: ')
        if a == "q": 
                break
        else:
                if (a.startswith("A") or a.startswith("a")): 
                        if ( dict_.get(a.lower()) == None ): 
                                print(f"{a} not found in Dictionary")
                        else:   
                                print(f"{a} : {dict_.get(a.lower())}") 
                                with open ('C:/Users/User/Desktop/words.txt', 'a') as f:  
                                        if (a.lower() not in words): 
                                                words.append(a.lower()) 
                                                f.write(a.lower()+'\n') 
                                        f.close() 
                else:
                        print("Input not started with 'a'.\n\t Try again")