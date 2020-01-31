# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:05:23 2019

@author: agnib
"""
lst = []

while True:
    num = input("Enter List Value :  ")
    if(num=="STOP"):
        break
    else:
        lst.append(int(num))
        
print(lst)
largest = 0

for x in lst:
    if(x>largest):
        largest=x


print("\nLargest Number : ",largest)