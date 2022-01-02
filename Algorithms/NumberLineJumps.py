#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    while(x1 != x2):
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"
        elif (x1 > 10000 or x2 > 10000):
            return "NO"
