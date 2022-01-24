from sys import stdin

loop = int(stdin.readline())
sort = list()
for _ in range(loop):
    sort.append(int(stdin.readline()))

sort.sort()

for i in sort:
    print(i)
