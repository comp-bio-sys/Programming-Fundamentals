# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:01:02 2021

@author: User
"""


Cities=['Nur-Sultan','Almaty','Seoul','Alanya','Alexandria','Kempton Park','Aguascalientes']
l1=0
max_ind=-1;
for i in range(len(Cities)):
    word=Cities[i].lower()
    start=0
    end=len(word)-1
    if word[start]!=word[end]:
        continue;
    else:
     for k in range(len(word)):
          if word[k]==' ' or word[k]=='-':
             break
          else:
             pass;
     if k==len(word)-1:
         if(l1<len(word)):
            l1=len(word)
            max_ind=i
     else:
        pass
print("The longest name of the city is %s.It consists of %d characters." %(Cities[max_ind],l1))