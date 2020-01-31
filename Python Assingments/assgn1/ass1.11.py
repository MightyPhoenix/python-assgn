# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:00:14 2019

@author: agnib
"""
sum = 0 
GROCERY = {"Water" : 500,
           "Air" : 960,
           "Food" : 1700,
           "Shelter" : 30000,
           "Internet" : 20
           }

print("The Items with their Prices : \n")

print(GROCERY)
    
sum = GROCERY["Water"]+GROCERY["Air"]+GROCERY["Food"]+GROCERY["Shelter"]+GROCERY["Shelter"]

print("\nTotal Bill is : ",str(sum))