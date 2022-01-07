#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#
# A jail has a number of prisoners and a number of treats to pass out to them. 
# Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. 
# A chair number will be drawn from a hat. Beginning with the prisoner in that chair, 
# one candy will be handed to each prisoner sequentially around the table until all have been distributed.
# The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. 
# Determine the chair number occupied by the prisoner who will receive that candy.

def saveThePrisoner(n, m, s):
    # Write your code here
    result = ((m + s - 1) % n)
    if result == 0:
        return n
    else:
        return result
