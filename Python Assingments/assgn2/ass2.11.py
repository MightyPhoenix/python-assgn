# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:17:55 2019

@author: agnib
"""

happy = []
sad = []
neutral = []

while True:
    
    a=str(input("Enter you MOOd (happy,sad,nuetral) : "))
    
    if(a=='happy'):
        word=str(input("Enter a word for Happy : "))
        happy.append(word)
    elif(a=='sad'):
        word=str(input("Enter a word for Sad : "))
        sad.append(word)
    elif(a=='neutral'):
        word=str(input("Enter a word for Neutral : "))
        neutral.append(word)
    elif(a=='no'):
        break

print(happy)
print(sad)
print(neutral)