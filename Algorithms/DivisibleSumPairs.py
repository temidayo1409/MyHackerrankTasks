#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    num_of_pairs = 0
    for i in range(n):
        m = i + 1
        for j in range(m, n):
            if((ar[i]+ar[m]) % k == 0):
                num_of_pairs += 1
            m += 1
    return num_of_pairs
