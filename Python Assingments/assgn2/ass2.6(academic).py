# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:20:00 2019

@author: agnib
"""

binary=[]
reverse=[]
while True:
    
    Y=(input("enter binary: "))
    
    if (Y=="stop"):
        break
    else:
        binary.append(int(Y))
print(binary)
reverse=binary[::-1]
y=len(binary)

Sum=0
for i in range(y):
    if (reverse[i]==1):
        Sum=Sum + (reverse[i]*(2**i))
print("decimal: ",Sum)
