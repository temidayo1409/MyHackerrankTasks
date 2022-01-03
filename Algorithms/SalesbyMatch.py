#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sorted_ar = sorted(ar)
    dict_ar = {}
    num_pairs = 0
    for i in sorted_ar:
        if(i in dict_ar):
            dict_ar[i] += 1
        else:
            dict_ar[i] = 1
    for values in dict_ar.values():
        if(values >= 2):
            num_pairs += (values//2)
    return num_pairs
