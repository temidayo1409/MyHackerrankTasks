#!/bin/python3

import math
import os
import random
import re
import sys
from array import *

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    c = array('i',[0,0])
    for i in range(len(a)):
        if a[i] > b[i]:
            c[0] += 1
        elif a[i] < b[i]:
            c[1] += 1
    return c
