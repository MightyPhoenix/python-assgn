# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:15:28 2019

@author: agnib
"""

lst = []

while(True):
    val=input("Enter list element : ")
    if(val!='exit'):
        lst.append(int(val))
    else:
        break

search=int(input("\nEnter Element to search : "))

for i in lst:
    if(i==search):
        print("\nElement found : ",i)
        lst.remove(i)
        print("\nNew List: ",lst)
        break

    