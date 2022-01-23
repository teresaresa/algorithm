from sys import stdin

tc = int(stdin.readline())
for i in range(tc):
    ab = list(map(int, stdin.readline().split()))
    print(sum(ab))
