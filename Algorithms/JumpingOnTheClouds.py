#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.

# A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. 
# The character must jump from cloud to cloud until it reaches the start again.
# There is an array of clouds, c and an energy level e = 100. The character starts from c[0] and uses 1 unit of 
# energy to make a jump of size k to cloud c[(i+k) % n]. 
# If it lands on a thundercloud, c[i] = 1, its energy (e) decreases by 2 additional units. The game ends when the character lands back on cloud 0.
# Given the values of n, k, and the configuration of the clouds as an array c, determine the final value of e after the game ends

def jumpingOnClouds(c, k):
    e = 100
    i = 0
    n = len(c)
    while True:
        if (i+k) % n == 0:
            if c[(i+k) % n] == 1:
                e -= 2
            e -= 1
            i = (i+k) % n
            break
        elif c[(i+k) % n] == 1:
            e -= 3
            i = (i+k) % n
        else:
            e -= 1
            i = (i+k) % n
    return e
