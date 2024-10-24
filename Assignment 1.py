# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
1. How many digits, capital and lowercase letters are included in input argument? Create the function, i.e., fun_1, to print out the outputs as 
below: 

**Input**
- fun_1("aDbAc1d5ef")<br>

**Output** <br>
 2 digit letters found <br>
 2 upper letters found <br>
 6 lower letters found <br>
'''


def fun_1(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
           d["upper"]+=1
        elif c.islower():
           d["lower"]+=1
        else:
           pass
    num=0
    for a in s:
        if a.isdigit():
            num=num+1
        else:
            pass
    print(num," Digits letter found")
    print (d["upper"]," upper letters found")
    print (d["lower"]," lower letters found")

fun_1("aDbAc1d5ef")

'''
2. We have a list variable 'n' which has various data types of element, (i.e., n = ['3', 'a', 'e', 'f', 'g', '4', '!', '@', 'e', 'A', 'B', 'a']). 
Classify the individual elements into 'odd_number', 'even_number', 'lower_letter', 'upper_letter', and 'special_letter'. Create a funtion (fun_2) 
which returns five list type variables 'odd_N', 'even_N', 'lower_L', upper_L, and 'Special_L'. Note that dupulicated element must be removed so 
that all the elements should be unique.
Input

arg1 = ['3', 'a', 'e', 'f', 'g', '4', '!', '@', 'e', 'A', 'B', 'a']
odd_number, even_number, upper_Letter, lower_Letter, special_letter = fun_2(arg1)
print(odd_number,'\n', even_number,'\n', upper_Letter,'\n', lower_Letter,'\n', special_letter)
Output
['3']
['4']
['A', 'B']
['a', 'e', 'f', 'g']
['!', '@']
'''

def fun_2(arg1):
    odd_number = []
    even_number = []
    upper_letter = []
    lower_letter = []
    special_letter = []
    for x in arg1:
        if x.isupper():
            if x not in upper_letter:
                upper_letter.append(x)
        elif x.islower():
            if x not in lower_letter:
                lower_letter.append(x)
        elif x.isnumeric():
            if int(x)%2 == 0 and x not in even_number:
                even_number.append(x)
            elif int(x)%2 != 0 and x not in odd_number:
                odd_number.append(x)
        else:
            if x not in special_letter:
                special_letter.append(x)
    
    return odd_number, even_number, upper_letter, lower_letter, special_letter


arg1 = ['3','a','e','f','g','4','!','@','e','A','B','a']
odd_number, even_number, upper_letter, lower_letter, special_letter = fun_2(arg1)
print(odd_number,'\n',even_number,'\n',upper_letter,'\n',lower_letter,'\n',special_letter)


'''
3. Given the array of string values, find the longest and shortest strings in that array. Create a function (fun_3) to print out the both 
strings and its length. If multiple strings with the same length are found, write only one of them.

'''

languages = ['Python','Java','JavaScript','Go','Ruby','Dart',
             'PHP','Scala','Kotlin','Rust','C++','C','Haskell']
def fun_3(arg1):
    min_s=arg1[0]
    max_s=arg1[0]
    for a in arg1:
        if len(a)<len(min_s):
            min_s=a
        if len(a)>len(max_s):
            max_s=a
    print('longest string is "'+max_s+'" and its length is:',len(max_s))
    print('shortest string is "'+min_s+'" and its length is:',len(min_s))

languages=['Python','Java','JavaScript','Go','Ruby',
           'Dart','PHP','Scala','Kotlin','Rust','C++','C','Haskell']
fun_3(languages)

'''
4. Create one random number using random function (i.e., secret number) ranged between -100000 to 100000. A computer has to initially guess 
the secret number by also creating a random number (i.e., guess number). The program informs the computer whether the guessed number is larger, 
smaller or equal to the secret number. According to the program's feedback, computer should properly update the guess number. The program should 
be finished when the computer correctly guess the secret number. Create the fun_4 and your program should be able to search the secret number in 
reasonable iterations (computational cost).

'''

def fun_4(secret_number,guess_number,max_,min_):
    if guess_number==secret_number:
        print("You won!")
        return
    if guess_number>secret_number:
        print("Number is too large")
        max_ = guess_number-1
    else:
        print("Number is too small")
        min_ = guess_number+1
    guess_number = (min_+max_)//2
    print("guessing number is updated as:",guess_number)
    fun_4(secret_number,guess_number,max_,min_)

import random
max_ = 100000
min_ = -100000
secret_number = random.randrange(min_,max_)
guess_number = random.randrange(min_,max_)
print("secret number is:",secret_number)
print("initial guessing number is:",guess_number,'\n')

fun_4(secret_number,guess_number,max_,min_)



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Important
your code should be working at the cell below

Do not make your code creating the error in the cell below. If you code is incomplete then make 
your function as comment (see the first line) and we will take a loot your code for patial points. 
If your code makes error then you will get -3 point on individual function.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# fun_1("aDbAc1d5ef")   # this code is incomplete




