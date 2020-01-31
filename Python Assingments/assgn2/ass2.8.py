# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:40:20 2019

@author: agnib
"""

for i in range(1,501):
    if(i%3==0 and i%5==0):
        print(str(i)," FizzBuzz")
    elif(i%3==0):
        print(str(i)," Fizz")
    elif(i%5==0):
        print(str(i)," Buzz")
    