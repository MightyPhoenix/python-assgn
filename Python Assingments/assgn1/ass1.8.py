# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:54:09 2019

@author: agnib
"""

income = float(input("Enter Income in Lakhs (e.g. 5.5) to Calc. Tax : "))

if(income<=1.5):
    print("No TAX for you!")

elif(income>1.5 and income<=3):
    tax = (income*10)/100
    print("Tax : "+str(tax)+" Lakhs")

elif(income>3 and income<=5):
    tax = (income*20)/100
    print("Tax : "+str(tax)+" Lakhs")

elif(income>5):
    tax = (income*30)/100
    print("Tax : "+str(tax)+" Lakhs")
    
else:
    print("BYE")