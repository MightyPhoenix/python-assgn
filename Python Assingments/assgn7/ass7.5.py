# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:21:44 2019

@author: agnib
"""

import matplotlib.pyplot as plt
import random
hobbies=['singing','dancing','reading','programming','hacking']
student=[]
fr=[]

for i in range(60):student.append(random.choice(hobbies))
for i in hobbies:fr.append(student.count(i))

plt.pie(fr,  labels=hobbies, 
        colors=['red','green','yellow','lightcoral', 'lightskyblue']
        ,autopct='%1.1f%%')
