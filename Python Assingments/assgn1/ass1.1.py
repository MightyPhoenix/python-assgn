# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:28:37 2019

@author: agnib
"""
import math

print("Enter 3 sides of the triangle : ")

a=int(input("Enter a = "))
b=int(input("Enter b = "))
c=int(input("Enter c = "))

if (a+b>c and a+c>b and b+c>a):
    s = (a+b+c)/2
    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print("Area is : "+str(area))

else:
    print('Error')
    
    
    

