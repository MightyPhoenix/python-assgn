# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:16:21 2019

@author: agnib
"""

palin=[]
pri=[]
nat=[]

for num in range(500):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
        if(temp==rev):
            palin.append(temp)
  
    
for val in range(500):   
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else:
           pri.append(val)

for n in range(500):
    nat.append(n)
           
           
s_palin=set(palin)
s_pri=set(pri)
s_nat=set(nat)

print(s_palin.intersection(s_pri))
print("\n\n")
print(s_pri.difference(s_palin))
print("\n\n")
print(s_palin.difference(s_pri))
print("\n\n")
print(s_nat.difference(s_pri,s_palin))
