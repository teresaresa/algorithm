from sys import stdin


# https://www.acmicpc.net/problem/10989
i = int(stdin.readline())
t = [0] * 10001
for j in range(i):
    k = int(stdin.readline())
    t[k] += 1

for j, k in enumerate(t):
    if k >= 1:
        for l in range(k):
            print(j)
