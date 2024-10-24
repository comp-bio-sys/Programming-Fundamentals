# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:05:05 2021

@author: User
"""
def write_file (my_file,my_str,num):
    wr = open(my_file,"w")
    for i in range(1,num+1):
        wr.write(my_str+"_"+str(i)+"\n")
    wr.close()
    read = open(my_file,"r")
    all_lines = read.readlines()
    for line in all_lines:
       print(line.replace("\n",""))
    print("\n"+ all_lines[-2])

write_file('mytest.txt',"Waltz bad nymph for quick jigs vex",4)


def append_file(my_file, my_str, num):

   
    
    with open(my_file,'a+') as f:
    
        print(f.tell())
        
        f.write(my_str) 
        
        f.seek(0) 
        
        lines = f.readlines() 
    
        for i in range(min(len(lines), num)):
        
            print(lines[i])


my_file = 'mytest.txt'

my_str = 'With tenure,\nSuzie^d  have all the more leisure for yachting,\nbut her publications are no good'
write_file('mytest.txt',"Waltz bad nymph for quick jigs vex",3)
append_file(my_file, my_str, 5)


