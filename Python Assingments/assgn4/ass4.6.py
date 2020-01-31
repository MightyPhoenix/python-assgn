# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:31:45 2019

@author: agnib
"""

from statistics import mean

frenz = ["Rohit","Rahul","Rohan","Rini","Ronit","Rakesh","Roshan","Rupert"]

height = [1.56,2.0,1.65,1.87,1.43,1.98,1.66]

maxheight=max(height)
maxheightindex=height.index(maxheight)
name=frenz[maxheightindex]
print("Max Height : ",name,maxheight)

minheight=min(height)
minheightindex=height.index(minheight)
name2=frenz[minheightindex]
print("Min Height : ",name2,minheight)

avg=mean(height)
print("Average Height : ",avg)