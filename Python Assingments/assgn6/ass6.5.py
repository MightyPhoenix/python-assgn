# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:26:55 2019

@author: agnib
"""
import random

words={
       "muricide":"killing or killer of mice or rats",
       "acrophonic":"using a symbol for the initial sound of a thing",
       "mogadore":"ribbed silk used in making neckties",
       "zebrule":"hybrid offspring of male zebra and female horse",
       "cachinnate":"to laugh loudly and inappropriately",
       "wiredraw":"to reduce fluid pressure by passing it through a small orifice",
       "crystallomancy":"divination by means of clear objects",
       "thanatism":"belief that the soul dies with the body",
       "isograph":"line connecting points of same linguistic usage in some respect",
       "timbrophily":"love or fondness for stamps; stamp-collecting"
       }

vals=[]
for x in words.values():
    vals.append(x)

choice=random.choice(vals)

print(choice)
ans=input("Guess the word : ")

for word,mean in words.items():
    if ans==word:
        print("Your Answer is Correct!")
    elif choice==mean:
        print("Correct answer is ",word)
        