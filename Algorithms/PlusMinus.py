#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    np = 0
    nn = 0
    nz = 0
    for i in arr:
        if i > 0:
            np += 1
        elif i < 0:
            nn += 1
        else:
            nz += 1
    print("{:.6f}".format(np/len(arr)))
    print("{:.6f}".format(nn/len(arr)))
    print("{:.6f}".format(nz/len(arr))) 
