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
    parse_s = datetime.strptime(s, "%I:%M:%S%p")
    parse_s_form = datetime.strftime(parse_s, "%H:%M:%S")
    return parse_s_form
