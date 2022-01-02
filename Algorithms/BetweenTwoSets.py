#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    num_int = 0
    for i in range(1, 101):
        if all(i%x == 0 for x in a) and all(y%i == 0 for y in b):
            num_int += 1
    return num_int
