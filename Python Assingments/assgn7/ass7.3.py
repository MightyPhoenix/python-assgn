# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:16:52 2019

@author: agnib
"""

from matplotlib import pyplot as plt
import random
student=[]
grade=[]
for i in range(60):student.append(random.choice(['A','B','C','D','O','E']))
for i in ['A','B','C','D','O','E']:grade.append(student.count(i))
plt.bar(['A','B','C','D','O','E'],grade)