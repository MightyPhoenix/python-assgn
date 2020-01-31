# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:39:42 2019

@author: agnib
"""

import module2

ins=int(input('''Enter Your Choice :\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Square Root\n\nChoice : '''))

if(ins==1):
    a=float(input("Enter 1st number : "))
    b=float(input("Enter 2nd number : "))
    print(module2.add(a,b))
if(ins==2):
    a=float(input("Enter 1st number : "))
    b=float(input("Enter 2nd number : "))
    print(module2.subt(a,b))
if(ins==3):
    a=float(input("Enter 1st number : "))
    b=float(input("Enter 2nd number : "))
    print(module2.mult(a,b))
if(ins==4):
    a=float(input("Enter 1st number : "))
    b=float(input("Enter 2nd number : "))
    print(module2.div(a,b))
if(ins==5):
    a=float(input("Enter 1st number : "))
    b=float(input("Enter 2nd number : "))
    print(module2.mod(a,b))
if(ins==6):
    a=float(input("Enter 1st number : "))
    b=float(input("Enter 2nd number : "))
    print(module2.sqrt(a,b))