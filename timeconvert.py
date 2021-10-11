#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_s = datetime.strptime(s, "%I:%M:%S%p")
    #strftime converts datetime object to string
    #syntax is datetime.strptime(date_string, format)
    new_time = datetime.strftime(time_s, "%H:%M:%S")
    #strptime converts string to datetime object
    print(new_time)

s = input()
timeConversion(s)
