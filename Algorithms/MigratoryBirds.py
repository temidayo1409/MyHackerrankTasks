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
    arr_freq = [0] * len(arr)
    freq_id = []

    for i in range(len(arr)):
        arr_freq[arr[i]] += 1 
    for j in range(len(arr_freq)):
        if(arr_freq[j] == max(arr_freq)):
            freq_id.append(j)
    return min(freq_id)
