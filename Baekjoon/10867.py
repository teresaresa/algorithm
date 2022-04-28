from sys import stdin

number = list()

x = int(stdin.readline())
y = list(map(int, stdin.readline().split()))

for z in y:
    if z not in number:
        number.append(z)

number.sort()
print(' '.join(str(i) for i in number))
