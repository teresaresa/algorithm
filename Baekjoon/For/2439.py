from sys import stdin

n = int(stdin.readline())
for i in range(1, n+1):
    x = 0
    for j in range(1, n+1):
        t = " " if i < n-x else "*"
        x += 1
        print(t, end="")
    print()
