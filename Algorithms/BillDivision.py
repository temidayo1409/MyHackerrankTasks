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
    anna_pay = (sum(bill) - bill[k])//2
    if(anna_pay == b):
        print("Bon Appetit")
    else:
        print(b - anna_pay)
