#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app_sum = 0
    ora_sum = 0
    for i in apples:
        i += a
        if i in range(s, t+1):
            app_sum += 1
    for j in oranges:
        j += b
        if j in range(s, t+1):
            ora_sum += 1
    print(app_sum)
    print(ora_sum)
