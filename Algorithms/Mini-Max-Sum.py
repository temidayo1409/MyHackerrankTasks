import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr_sort = sorted(arr)
    rev_arr_sort = sorted(arr, reverse = True)
    min_sum = 0
    max_sum = 0
    for i in range(len(arr) - 1):
        min_sum += arr_sort[i]
    for i in range(len(arr) - 1):
        max_sum += rev_arr_sort[i]
    print(min_sum, max_sum)
