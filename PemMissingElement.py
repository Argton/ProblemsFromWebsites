# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 02:31:01 2018
This function takes an array of integers from 1:N+1, where N is the size of
the array. One of these numbers are missing and the program finds it.
@author: Anton
"""

def PermMissingElement(A):
    val=0
    A.sort()
    if A == None or len(A) == 0:
        return 1
    if len(A)==1:
        if A[0]==1:
            return 2
        else:
            return 1
    for j in range(0, len(A)):
        if j+1 != A[j]:            
            return j+1
    else:
        return A[len(A)-1]+1
    
A=[2,1]
print(PermMissingElement(A))
        