# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:33:03 2019

@author: agnib
"""

class Stack:
    stack=[]
    top=0
    
myStack=Stack()

def pop():
    if(myStack.top==0):
        print("UnderFlow")
        return
    print(myStack.stack.pop())
    myStack.top-=1
    
def push(a):
    myStack.stack.append(a)
    myStack.top+=1
    
def display():
    if myStack.top==0:
        print("Empty Stack")
        return
    print(myStack.stack)
    
    
while True:
    op=input("Enter Operation you want to perform , enter exit to exit : ")
    print(myStack.top)
    if "pop"==op:
        pop()
    elif "display"==op:
        display()
    elif "push"==op:
        e=int(input("Enter Element : "))
        push(e)
    elif "exit"==op:
        break
    else:
        print("Invalid Command")
