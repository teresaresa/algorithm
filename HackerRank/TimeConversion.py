#!/bin/python3
# https://www.hackerrank.com/challenges/time-conversion/problem

import os
import sys


def timeConversion(s):
    splittedAry = s.split(':')

    minutes = splittedAry[1]
    seconds = splittedAry[2][0:2]

    # AM/PM
    lastElement = splittedAry.pop()

    if lastElement[2:4] == 'PM':
        hour = int(splittedAry[0]) + 12 if int(splittedAry[0]) != 12 else int(splittedAry[0])
    else:
        hour = '00' if int(splittedAry[0]) == 12 else splittedAry[0]

    return '{}:{}:{}'.format(hour, minutes, seconds)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
