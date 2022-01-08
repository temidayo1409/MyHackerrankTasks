#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#
# John Watson knows of an operation called a right circular rotation on an array of integers. 
# One rotation operation moves the last array element to the first position and shifts all remaining elements right one. 
# To test Sherlock's abilities, Watson provides Sherlock with an array of integers. 
# Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.
# For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

def circularArrayRotation(a, k, queries):
    # Write your code here
    
    # My first solution (failed one test case):
    #AfterRotate = [0] * len(a)
    #result = []
    #for i in range(len(a)):
    #    if((i + k) < len(a)):
    #        AfterRotate[i + k] = a[i]
    #    else:
    #        AfterRotate[(i + k) - len(a)] = a[i]
    #return (AfterRotate[x] for x in queries)

    # Second solution:
    n = len(a)
    result = []
    for i in queries:
        result.append(a[(n - k + i) % n])
    return result
