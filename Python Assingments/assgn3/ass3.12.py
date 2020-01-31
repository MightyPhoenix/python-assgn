# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:19:48 2019

@author: agnib
"""

HAPPY = []
SAD = []
NEUTRAL = []

while(True):
    word=str(input("Enter a Word or 'exit' : "))
    
    if(word!='exit'):
        print("\n\n1. HAPPY // 2. SAD // 3. NEUTRAL\n")
        lst=int(input("Enter Choice : "))
        
        if(lst==1):
            HAPPY.append(word);
        elif(lst==2):
            SAD.append(word);
        elif(lst==3):
            NEUTRAL.append(word);
    
    else:
        print("\n\nHappy : ",HAPPY," SAD : ",SAD," Neutral : ",NEUTRAL)
        break