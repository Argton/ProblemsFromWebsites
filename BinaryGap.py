# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:45:20 2018
This program converts an int into its binary representation, except for the beginning "0b".
It then looks for and returns the largest gap, being defined as the number of zeros between two ones.
For example the binary number "1001" has a gap of two.
@author: Anton
"""

def BinGap(myint):
    mystr1=bin(myint)
    mystr2=mystr1[2:]
    gaplist=[0]
    for number in range(0, len(mystr2) - 1):
        if mystr2[number]=="1":
            gap=0
            for nr in range(number + 1, len(mystr2)):
                if mystr2[nr]=="0" and nr<len(mystr2):
                    gap+=1
                elif mystr2[nr]=="1":
                    gaplist.append(gap)
                    break
    return(max(gaplist))

  
    
S=1376796946
print(bin(S)) # Check solution
print(BinGap(S))