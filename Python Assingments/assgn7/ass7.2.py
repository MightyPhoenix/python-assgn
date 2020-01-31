# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:15:36 2019

@author: agnib
"""

from matplotlib import pyplot as plt
import random
age=[]
for i in range(50):age.append(random.randint(25,60))
plt.hist(age,bins=8,range=(25,60),color='green')