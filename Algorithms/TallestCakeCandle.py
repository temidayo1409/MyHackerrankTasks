#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    num_tallest = 1
    sort_candles = sorted(candles, reverse = True)
    for i in range(1, len(sort_candles)):
        if sort_candles[i] == sort_candles[0]:
            num_tallest += 1
    return num_tallest
