from sys import stdin


# https://www.acmicpc.net/problem/2577
cal = 1
for i in range(3):
    j = int(stdin.readline())
    cal *= j

base = [0] * 10
for i in str(cal):
    i = int(i)
    base[i] += 1

for i in base:
    print(i)
