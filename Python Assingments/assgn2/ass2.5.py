# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:13:10 2019

@author: agnib
"""

start=input("enter start day of month : ")
number=int(input("enter number of days : "))
week={"sunday":"0",
      "monday":"1",
      "tuesday":"2",
      "wednesday":"3",
      "thursday":"4",
      "friday":"5",
      "saturday":"6"}

start=int(week[start])
print("S  M  T  W  T  F  S")

for i in range(0,start):
    print("   ",end="")
for i in range(1,7-start+1):
    print(str(i)+"  ",end="")
print()

for i in range(7-start+1,number+1):
    if(len(str(i))==1):
        print(str(i)+"  ",end="")
    elif(len(str(i))==2):
        print(str(i)+" ",end="")
    if i in range(7-start,number+1,7):
        print()
print()
