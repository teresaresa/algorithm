from sys import stdin

tc = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().split()))

result = list()
for n in numbers:
    if n < tc[1]:
        result.append(n)

for r in result:
    print(r, end=" ")
print()
