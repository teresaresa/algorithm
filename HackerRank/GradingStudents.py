#!/bin/python3
# https://www.hackerrank.com/challenges/grading/problem

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def calcNearest(multiple, grade, loop=20):
    results = 0

    for i in range(0, loop):
        calculate = multiple * (i + 1)

        if calculate > grade:
            results = calculate
            break

    return results


def gradingStudents(grades):
    # Write your code here
    multiple = 5
    cutline = 40

    results = list()
    for grade in grades:
        nGrade = calcNearest(multiple, grade)

        if grade < 38:
            pass

        elif nGrade < cutline:
            pass

        elif nGrade - grade < 3:
            grade = nGrade

        results.append(grade)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
