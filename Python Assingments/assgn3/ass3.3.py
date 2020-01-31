# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:13:28 2019

@author: agnib
"""

def simpleInt(age,money,time):
    if(age>=60):
        simpleInterest=(money*time*0.12)
        return simpleInterest
    else:
        simpleInterest=(money*time*0.10)
        return simpleInterest

age = int(input("Enter your Age : "))
money = int(input("Enter Amount of Money : "))
time = int(input("Enter time in Years : "))

simpl = simpleInt(age,money,time)

print("\nSimple Interest : ",simpl)
