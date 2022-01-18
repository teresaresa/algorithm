from sys import stdin
import math

# https://www.acmicpc.net/problem/10250
t = int(stdin.readline())
for loop in range(t):
    h, w, n = map(int, stdin.readline().split())

    floor = math.ceil(n/h)
    compare = abs(floor*h - n)

    result1 = 0
    result2 = format(floor, '02')
    for check in range(1, h+1):
        h -= 1
        if h == compare:
            result1 = check
            break

    print(f'{result1}{result2}')
