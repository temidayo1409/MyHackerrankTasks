#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    num_of_ways = 0
    for i in range(len(s) - m + 1):
        sums = 0
        k = i
        for j in range(m):
            sums += s[k]
            k += 1
        if sums == d:
            num_of_ways += 1
    return num_of_ways
