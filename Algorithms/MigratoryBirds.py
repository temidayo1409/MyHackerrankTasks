#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    freq = {}
    list_id = []
    for i in arr:
        if (i in freq):
            freq[i] += 1
        else:
            freq[i] = 1
 
    for key, value in freq.items():
        if(value == max(freq.values())):
            list_id.append(key)
    return min(list_id)
