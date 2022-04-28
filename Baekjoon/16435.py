from sys import stdin

count, length = list(map(int, stdin.readline().split()))
fruits = list(map(int, stdin.readline().split()))

fruits.sort()

for fruit in fruits:
    if fruit <= length:
        length += 1

print(length)
