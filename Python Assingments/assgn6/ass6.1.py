# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:49:01 2019

@author: agnib
"""

teachC = {'a','b','c','p','d','e','f','g','h','i'}
teachS = {'a','m','n','c','i'}

print(f"All teachers who have taken my class : {teachS.union(teachC)}")
print(f"All teachers who have not take your class : {teachC.difference(teachS)}")
print(f"All teachers who have taken class in school : {teachS}")
