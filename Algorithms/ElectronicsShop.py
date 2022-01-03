#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
# A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with
# a given budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    buy_price = 0
    for i in keyboards:
        for j in drives:
            if(i + j <= b and i + j > buy_price):
                buy_price = i + j
    if(buy_price == 0):
        return -1
    else:
        return buy_price
