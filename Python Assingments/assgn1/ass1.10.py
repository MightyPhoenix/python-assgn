# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:19:25 2019

@author: agnib
"""
from operator import add

l1 = [1,2,3,4,5]
l2 = l1[::-1]

print(list(map(add,l1,l2)))