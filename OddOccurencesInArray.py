# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 02:23:49 2018
This function takes an array filled with pairs of elements
and one loner element. The task is to find this loner element.
@author: Anton
"""

def OccOccurence(A):
    A.sort()
    val=0
    if len(A)==1:
        return A[0]
    for i in range(0, len(A)//2):
        if A[2*i] != A[2*i +1]:
            val = A[2*i]
            break
        val = A[len(A)-1]
    return val