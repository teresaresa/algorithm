from sys import stdin

n = int(stdin.readline())
p = list(map(int, stdin.readline().split()))

p.sort()

sum = 0
for i in range(n):
    sum += p[i] * (n-i)

print(sum)
