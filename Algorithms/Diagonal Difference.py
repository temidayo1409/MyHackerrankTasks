import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    pd = 0
    sd = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                pd += arr[i][j]
            if i == len(arr) - j - 1:
                sd += arr[i][j]
    return abs(pd - sd)
