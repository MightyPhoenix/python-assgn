# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:07:49 2019

@author: agnib
"""

#mappin'

def intify(n):
    return int(n)

some=input("here : ")

listy= list(some)
inted=map(intify,listy)

biner=list(reversed(list(inted)))

dec = 0 

for i in range(len(biner)):
    dec = dec + (biner[i]*(2**i))
    
print(dec)