# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:46:02 2019

@author: agnib
"""

size = int(input("Enter List Size : "))
list = []
sum = 0

for x in range(size):
    value=int(input())
    list.append(value)

print(list)

for i in range(size):
    sum = sum+list[i]
    
print("Sum : ",sum)

