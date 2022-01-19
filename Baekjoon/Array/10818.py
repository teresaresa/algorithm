from sys import stdin


i = stdin.readline()
j = stdin.readline()

min = 1000001
max = -1000001
for k in j.split():
    k = int(k)
    min = k if k <= min else min
    max = k if k >= max else max

print(f'{min} {max}')
