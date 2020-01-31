# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:03:04 2019

@author: agnib
"""

exam1 = int(input("Enter marks out of 100 for exam1 : "))
exam2 = int(input("Enter marks out of 100 for exam2 : "))

sport = int(input("Enter marks out of 50 for sport : "))

act1 = int(input("Enter marks out of 20 for Activity 1 : "))
act2 = int(input("Enter marks out of 20 for Activity 2 : "))
act3 = int(input("Enter marks out of 20 for Activity 3 : "))

exam = exam1+exam2
act = act1+act2+act3

if (exam <=200 and sport <= 50 and act <= 60):
    
    exam = (exam/200)*100
    act = (act/60)*100
    sport = (sport/50)*100
    
    examf = (exam*50)/100
    sportf = (sport*20)/100
    actf = (act*30)/100
    
    total_stu = examf+sportf+actf
    
    print("Student's Marks is : "+str(total_stu))
    100
else:
    print("Try Again, Invalid Input!")


