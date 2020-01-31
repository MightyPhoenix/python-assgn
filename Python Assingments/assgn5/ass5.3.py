# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:21:41 2019

@author: agnib
"""

books=(('Panchatantra','Vishnu Sharma',350),
       ('Mahabharat','Vyasa',150),
       ('Ramayan','Valmiki',250))

while(True):
    bname=str(input("Enter Book Name : "))
    if(bname!='exit'):
        for i in books:
            if(i[0]==bname):
                print(f"BookName : {i[0]}  //  Author : {i[1]}  //  Price : {i[2]}  ")
    else:
        break