# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 11:54:57 2021

@author: User
"""

import random
import time

def write_updated_words(filename: str, words: list) -> None:
    f = open(filename, "w")
    for i in words:
        f.write(i + "\n")
    
    f.close()


words = open(r"C:/Users/User/Desktop/words.txt", "r")

words_list = [i.replace("\n", "") for i in words.readlines()]
words.close()


word_meanings = open(r'C:/Users/User/Desktop/DIC(A).txt', "r")

_dictionary = {}
for line in word_meanings.readlines():
    data = line.split(" ", 1)
    
    key = data[0].strip().lower() 
    value = (data[1:]) 
    _dictionary[key]=' '.join(value)
word_meanings.close()
guessed_word=""

while True:

   
    if guessed_word == "q" or len(words_list) == 0:
        print("no more words")
        break
  
    print("Meaning of the word:")
    ids = random.randint(0, len(words_list) - 1) 
    print(_dictionary[words_list[ids]])
    guessed_word = input("Put answer: ")


    if words_list[ids] == guessed_word:
        print("Correct\n\n")
        del words_list[ids]    
        write_updated_words(r"C:/Users/User/Desktop/words.txt", words_list)
    else:
        print("wrong")
        time.sleep(2)
        print(f"the word is : {words_list[ids]}\n")