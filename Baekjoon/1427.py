from sys import stdin

sort = list(map(int, stdin.readline().rstrip()))
sort.sort(reverse=True)

for i in sort:
    print(i, end="")
print()
