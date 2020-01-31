# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:52:09 2019

@author: agnib
"""

batsman = {'dhoni','virat kohl','sachin','gautam gambhir','rahul dravid','jadeja','laximane','maxwell','zampa','shaqib','avisek'}
bowler={'bumrah','bhubaneshwar','shaqib','zampa','jadeja','stark','malinga','shoaib','waqar','agnibesh','avisek'}

print(batsman.difference(bowler))
print(bowler.difference(batsman))
print(batsman.intersection(bowler))