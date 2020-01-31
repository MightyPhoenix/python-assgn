# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:07:06 2019

@author: agnib
"""

# Create an N x N magic square. N must be odd.
from tabulate import tabulate as tbl
import numpy as np

N = 9
magic_square = np.zeros((N,N), dtype=int)

i, j, n = 0, N//2, 1

while n <= N**2:
    magic_square[i, j] = n
    n += 1
    newi, newj = (i-1) % N, (j+1)% N
    if magic_square[newi, newj]:
        i += 1
    else:
        i, j = newi, newj

for i in magic_square:
    for j in i:
        print(j,end="  ")
        
    print("\n")


print(tbl(magic_square,tablefmt="grid"))