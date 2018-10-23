# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:31:33 2018
This program returns the longest password available in a given string.
The requirements are that there should only be alphanumerical characters,
an odd number of integers and an even number of letters. 
Otherwise it returns -1.

@author: Anton
"""


def LongestPassword(S):
   
    myString=S.split()
    values=[0]
    for word in myString:
        nbroflett=0
        nbrofints=0
        for letter in word:
            if letter in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
                nbroflett+=1
            if letter in "1234567890":
                nbrofints+=1
            if letter not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890":
                val=0
                break
        val=0
        if nbroflett%2==0 and nbrofints%2!=0 and nbrofints!=0:
            for letter in word:
                if letter in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890":
                    val=val+1
                else:
                    break     
            values.append(val)
    if max(values)>0:
        return max(values)
    else:
        return -1
    
    
S="1238j" ")#24ddj" "djd329" "dj923j" ")(3dsd)"

print(LongestPassword(S))