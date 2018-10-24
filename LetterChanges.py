# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 03:12:01 2018
This function increments all letters in a string by one and
capitalizes vowels.
@author: Anton
"""

def LetterChanges(str): 
    str2 = ""
    str3 = ""
    for letter in str:
        if letter == " ":
            str2+=" "
        elif letter == "Z":
            str2+="a"
        elif letter == "z":
            str2+="a"
        else: 
            str2+=chr(ord(letter)+1)
    for letters in str2:
        if letters in "aeoui":
            str3+=letters.upper()
        else:
            str3+=letters
    return str3

print LetterChanges(input())