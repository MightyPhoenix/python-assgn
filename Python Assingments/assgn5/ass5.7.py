# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:19:26 2019

@author: agnib
"""

animals=(("Dog",'land','bark','guard house'),
         ('Cat','land','meow','litter'),
         ('Cow','land','moo','grass eating'),
         ('Whale','water','whistle','swim'),
         ('Bird','air','chirp','fly'))

while(True):
    live=str(input("Enter where the Animals lives (land,water,air) : "))
    if(live!='exit'):
        sound=str(input("Enter animal sound : "))
        activity=str(input("Enter Animal activity : "))
        for i in animals:
            if(i[1]==live and i[2]==sound and i[3]==activity):
                print(f"\nYour Animal is : {i[0]}")
    else:
        break

    