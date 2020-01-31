# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:19:35 2019

@author: agnib
"""

a = int(input("Enter 1st Num = "))
b = int(input("Enter 2nd Num = "))


if(a==0 and b==0):
    print("GCD is 0\n")
elif(a==0):
    print("GCD is : ",b)
elif(b==0):
    print("GCD is : ",a)
else:
    if(a>b):
        small=b
    else:
        small=a
        
    for i in range(1,small+1):
        if(a%i==0 and b%i==0):
            gcd = i

print("gcd =",str(i))
            