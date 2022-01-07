#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#
# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, 
# the professor decides to cancel class if fewer than some number of students are present when class starts. 
# Arrival times go from on time (arrivalTime <= 0) to arrived late (arrivalTime > 0).
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is cancelled. 

def angryProfessor(k, a):
    # Write your code here
    counts = 0
    for i in a:
        if i <= 0:
            counts += 1
    if counts >= k:
        return "NO"
    else:
        return "YES"
