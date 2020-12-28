#!/bin/python3
# https://www.acmicpc.net/problem/10989

import sys

m = 10000
array = [0] * m

n = int(input())
for i in range(n):
    val = int(input())
    array[val-1] += 1

for val in range(m):
    while array[val] > 0:
        sys.stdout.write(str(val+1)+'\n')
        array[val] -= 1
