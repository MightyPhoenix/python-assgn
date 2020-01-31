# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:51:33 2019

@author: agnib
"""

import math

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

mean = (a+b)/2

dev = (math.sqrt((a-mean)**2+(b-mean)**2))/mean

print("Mean = "+str(mean))
print("The Standard Deviation = "+str(dev))