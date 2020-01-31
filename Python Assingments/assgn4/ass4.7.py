# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:19:27 2019

@author: agnib
"""

saarc = ["India","Pakistan","Bhutan","SriLanka","Afghanistan","Nepal","Maldives","Bangladesh"]

while(True):
    country=str(input("Enter Country : "))
    if(country!='exit'):
        if country in saarc:
            print("It is a Saarc Country")
        else:
            print("Not a saarc Country")
    else:
        break