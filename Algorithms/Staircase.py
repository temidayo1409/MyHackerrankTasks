#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    k = n - 1
    for i in range(n):
        for j in range(n):
            if j < k:
                print(" ", end = "")
            else:
                print("#", end = "")
        k -= 1
        print()
