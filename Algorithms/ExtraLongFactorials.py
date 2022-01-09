#!/bin/python3

import math
import os
import random
import re
import sys
from math import *

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#
# Calculate and print the factorial of a given integer.

def extraLongFactorials(n):
    # Write your code here
    
    # 1st method - just use the in-built "factorial" method:
    #print(factorial(n))
    
    # 2nd method:
    result = 1
    while(n > 0):
        result *= n
        n -= 1 
    print(result)
