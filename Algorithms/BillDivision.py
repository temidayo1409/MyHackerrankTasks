#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    sum_bill = 0
    for i in range(len(bill)):
        if(bill[i] == bill[k]):
            sum_bill += 0
        else:
            sum_bill += bill[i]
    anna_pay = sum_bill//2
    if(anna_pay == b):
        print("Bon Appetit")
    else:
        print(b - anna_pay)
