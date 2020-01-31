# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:52:12 2019

@author: agnib
"""

username = []
domain = []

for i in range(5):
    email=str(input(f"Enter Email No.{i}: "))
    usr,dom=email.split('@')
    username.append(usr)
    domain.append(dom)

print("Usernames : ",tuple(username))
print("Domains : ",tuple(domain))
    