# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:07:29 2019

@author: agnib
"""

def rev(n):
   if n<10:
      return n 
   else:
      return int(str(n%10) + str(rev(n//10)))


n=int(input("Enter a number: "))
print(rev(n))
