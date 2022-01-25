from sys import stdin

n = int(stdin.readline())
for case in range(1, n+1):
    result = sum(list(map(int, stdin.readline().split())))
    print(f'Case #{case}: {result}')
