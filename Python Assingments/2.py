# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:12:24 2019

@author: agnib
"""

username = []
domain = []

for i in range(1,6):
    email=str(input(f"Enter Email No.{i}: "))
    usr,dom=email.split('@')
    username.append(usr)
    domain.append(dom)
    
print("\n\nUsername : ",tuple(username))
print("\nDomain : ",tuple(domain))