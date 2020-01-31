# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:34:59 2019

@author: agnib
"""

def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0]

sent = str(input("Enter String : "))
print(reverse(sent))   