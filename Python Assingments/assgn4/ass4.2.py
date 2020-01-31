# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:59:26 2019

@author: agnib
"""

TOP = -1

stack = []

while(True):
    print("----STACK OPERATIONS-----\n1.Display\n2.Peek\n3.Pop\n4.Push")
    choice=int(input("Enter Choice : "))
    if(choice!=00):
        if(choice==1):
            print(stack)
        elif(choice==2):
            if(TOP<0):
                print("Stack Empty")
            else:
                print(stack[TOP])
        elif(choice==3):
            if(TOP<0):
                print("Stack Empty")
            else:
                TOP=TOP-1
                stack.pop()
        elif(choice==4):
            TOP=TOP+1
            ele=int(input("Enter Stack Element : "))
            stack.append(ele)
    else:
        break
        
        