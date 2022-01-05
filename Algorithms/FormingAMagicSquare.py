#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]

def formingMagicSquare(s):
    # Write your code here
    # There are five rules to take note for magic squares with 3x3 input:
    # ensure the center number is 5
    # The magic constant is 15
    # Magic constant = n(n2 + 1)/2
    # Even numbers should be at the 4 edges of the matrix
    # Odd numbers should be at the other positions (the center is already 5)
    # None of the numbers repeat i.e it consist of distinct numbers
    
    results = []
    for p in pre:
        total = 0
        for p_row, s_row in zip(p, s):
            for i, j in zip(p_row, s_row):
                if not i == j:
                    #total += max([i, j]) - min([i, j])
                    total += abs(i - j)
            
        results.append(total)
        
    return min(results)
    
