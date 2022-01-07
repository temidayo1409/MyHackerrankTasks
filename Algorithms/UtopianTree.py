#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
# The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after
growth cycles?

def utopianTree(n):
    # Write your code here
    height = 1
    for i in range(n+1):
        if i == 0:
            height = height
        elif i%2 == 0 or i == 1:
            height += 1 
        else:
            height *= 2
    return height
