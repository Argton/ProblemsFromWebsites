# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:35:46 2018
This programs takes a list A an rotates every element by one position,
K times.
@author: Anton
"""

def CyclRot(A, K):
    if len(A)==0 or K==0:
        return A
    else:
        for nbrOfTurns in range(0, K):
            tempArr=[]
            tempArr.append(A[len(A)-1])
            for index in range(0, len(A)-1):
                tempArr.append(A[index])
            A.clear()
            A=tempArr.copy()
    return tempArr

A=[1,2,3,4,5]
K=3

print(CyclRot(A, K))