#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase, ascii_uppercase

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#
# There is a list of 26 character heights aligned by index to their letters. 
# For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, 
# determine the area of the rectangle highlight in mm(square) assuming all letters are 1mm wide.

def designerPdfViewer(h, word):
    # Write your code here
    
    # 1st way to solve this:
    alphabets = ascii_lowercase
    dictionary = {}
    i = 0
    height = []
    for alphabet in alphabets:
        dictionary[alphabet] = h[i]
        i += 1
    for a, b in dictionary.items():
        for i in word:
            if a == i:
                height.append(b)
    return(max(height) * len(height))

    # 2nd way to solve this:
    #return len(word) * max(list(map(lambda x: h[ord(x) - ord('a')], word)))

    # 3rd way to solve this:
    #alphabets = ascii_lowercase
    #max_height = 0
    #for i in word:
    #    indexes = alphabets.index(i)
    #    max_height = max(max_height, h[indexes])
    #return (len(word) * max_height)
