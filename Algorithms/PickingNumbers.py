#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
#
# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

def pickingNumbers(a):
    # Write your code here
    result = 0
    checked = set()
    for i in range(len(a)):
        if i not in checked:
            maxCount = max(a.count(a[i]) + a.count(a[i] + 1), a.count(a[i])+                        a.count(a[i] - 1))
            if maxCount > result:
                result = maxCount
            checked.add(i)
    return result
