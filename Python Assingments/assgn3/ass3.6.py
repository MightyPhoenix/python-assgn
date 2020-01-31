# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:53:21 2019

@author: agnib
"""

def average(name,*marks):    

    str(name)
    lst = []
    for i in marks:
        lst.append(i)
    average=sum(lst)/len(lst)
    return print(f"{name} scored {lst} average is {average}")


average("Raj",80,70,80)
    