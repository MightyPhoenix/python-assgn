# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:33:20 2019

@author: agnib
"""

m = int(input("Enter Mass in Kg : "))
v = int(input("Enter Velocity m/s : "))

momentum = m*v
energy = m*v*v

print("Momentum is : "+str(momentum)+" Energy is : "+str(energy))