from sys import stdin
import math

a, b, v = list(map(int, stdin.readline().split()))
day = (v-b) / (a-b)

print(math.ceil(day))
