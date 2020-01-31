# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:49:47 2019

@author: agnib
"""
import random

Questions = {
        1: "What gets wetter the more it dries?",
        2: "What word is spelled incorrectly in every single dictionary?",
        3: "What never asks a question but gets answered all the time?",
        4: "What goes up but never ever comes down?",
        5: "What starts with “e” and ends with “e” but only has one letter in it?",
        6: "What has a face and two hands, but no arms or legs?",
        7: "What can be caught but never thrown?",
        8: "I start out tall, but the longer I stand, the shorter I grow. What am I?",
        9: "How many seconds are there in a year?",
        10: "What can run but not walk?"}

Answers = {
        1: "towel",
        2: "Incorrectly",
        3: "cellphone",
        4: "age",
        5: "envelope",
        6: "clock",
        7: "cold",
        8: "candle",
        9: "Twelve",
        10: "Raindrops"}

def play():
    choice=random.choice(list(Questions.keys()))
    ans=Answers[choice]
    print("\nQuestion: ",Questions[choice])
    pans=str(input("Answer : "))
    if(ans=='exit'):
        exit()
    elif(ans==pans):
        print("\nYou Won!")
        play()
    else:
        print("\nYou loose")
        play()
        

play()