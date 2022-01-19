from sys import stdin


# https://www.acmicpc.net/problem/2562
max_point = 0
max_value = 0
for i in range(1, 10):
    j = int(stdin.readline())
    if j > max_value:
        max_value = j
        max_point = i

print(max_value)
print(max_point)
