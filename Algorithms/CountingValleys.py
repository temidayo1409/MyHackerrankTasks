#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly STEPS steps,
# for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level, and each step up or down represents a 
# 1 unit change in altitude. We define the following terms:
# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through

def countingValleys(steps, path):
    # Write your code here
    track = 0
    no_of_valleys = 0
    for i in range(steps):
        if(path[i] == "D"):
            track -= 1
        else:
            track += 1
        if(track == 0 and path[i] == "U"):
            no_of_valleys += 1
    return no_of_valleys
