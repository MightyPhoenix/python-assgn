# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:39:07 2019

@author: agnib
"""

set1 = {('madhurima','painting'),
        ('arnab','photography'),
        ('agnibesh','music'),
        ('dipayan','comedy'),
        ('abhishek charan','robotics')}

set2 = {('akash','football'),
        ('madhurima,painting'),
        ('arnab','photography'),
        ('raghib','maths'),
        ('laxmi','voleyball')}

print(f"Set of all friends : {set1.union(set2)}\n")
print(f"Common friends in both school and college : {set1.intersection(set2)}\n")
if(set1.issuperset(set2)):
    print("Set1 is the superset of set2\n")
else:
    print("Set1 is not the superset of set2\n")
    