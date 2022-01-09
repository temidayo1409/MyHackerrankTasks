#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#
# Given a sequence of n integers, p(1), p(2),..., p(n) where each element is distinct and satisfies 1 <= p(x) <= n. 
# For each x where 1 <= x <= n, that is x increments from 1 to n, find any integer y such that p[p[y]] === x and keep a history of the values of y in a return array.

def permutationEquation(p):
    # Write your code here
    result = []
    for i in range(min(p), max(p) + 1):
        for j in range(len(p)):
            if p[p[j] - 1] == i:
                result.append(j + 1)
    return result
