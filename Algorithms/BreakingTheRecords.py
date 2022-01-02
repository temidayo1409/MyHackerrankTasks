#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    num_best = 0
    num_worst = 0
    smallest = scores[0]
    largest = scores[0]
    for i in range(1, len(scores)):
        if scores[i] < smallest:
            smallest = scores[i]
            num_worst += 1
        elif scores[i] > largest:
            largest = scores[i]
            num_best += 1
    return (num_best, num_worst)
