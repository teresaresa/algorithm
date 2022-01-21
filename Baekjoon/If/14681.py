from sys import stdin


x = int(stdin.readline())
y = int(stdin.readline())

if x > 0:
    print(1 if y > 0 else 4)
else:
    print(2 if y > 0 else 3)
