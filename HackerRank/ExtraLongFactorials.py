#!/bin/python3
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

import math
import os
import random
import re
import sys


def extraLongFactorials(n):
    calculate = n

    for i in range(1, n):
        calculate = calculate * (n - i)

    print(calculate)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
