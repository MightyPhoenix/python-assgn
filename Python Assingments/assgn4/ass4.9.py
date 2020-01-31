# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:35:58 2019

@author: agnib
"""

list1=["CSE","CIEM"]
list2=["IT","DEPT"]
list3=[]
for i in list1:
    for j in list2:
        k=i+" "+j
        list3.append(k)
print(list3)