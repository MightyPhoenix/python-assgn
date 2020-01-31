# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:11:35 2019

@author: agnib
"""

import math

print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == 0: 
    print("Invalid")

d = b * b - 4 * a * c 
sqrt_val = math.sqrt(abs(d)) 
      
if d > 0: 
    print((-b + sqrt_val)/(2 * a)) 
    print((-b - sqrt_val)/(2 * a)) 
    print("Roots are real and different ") 
elif d == 0: 
    print("Roots are real and same") 
    print(-b / (2*a)) 
else: #d<0 
    print("Roots are complex") 
    print(- b / (2*a) , " + i", sqrt_val) 
    print(- b / (2*a) , " - i", sqrt_val)