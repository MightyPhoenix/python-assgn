# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:05:32 2019

@author: agnib
"""

sports = {"badminton":["P.V. Sindhu","Saina Nehwal","Jwala Gutta"],
          "basketball":["Satnam Singh","Prashanti Singh"],
          "cricket":["Dhoni","Sachin","Sourav"],
          "football":["Sunil Chhetri","Gurpreet Singh Sandhu"]}

sport=input("Select a Sport : ")

players=sports.get(sport)

for ply in players:
    print("\n",ply)