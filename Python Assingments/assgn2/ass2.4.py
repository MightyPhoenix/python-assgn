# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 21:53:35 2019

@author: agnib
"""

num = int(input("Enter a Number : "))
factorial = 1

if num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       factorial = factorial*i  

print("The factorial of",num,"is",factorial)