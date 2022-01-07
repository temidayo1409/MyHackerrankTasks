#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#
#
# Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse.
# Given a range of numbered days, [i...j] and a number k, determine the number of days in the range that are beautiful. 
# Beautiful numbers are defined as numbers where |i - reverse(i)| is evenly divisible by k. If a day's value is a beautiful number, 
# it is a beautiful day. Return the number of beautiful days in the range.

def beautifulDays(i, j, k):
    # Write your code here
    the_list = []
    beautifulNums = []
    for x in range(i, j+1):
        the_list.append(abs(int(str(x)[::-1])) - x)
    for y in the_list:
        if(y%k == 0):
            beautifulNums.append(y)
    return len(beautifulNums)
