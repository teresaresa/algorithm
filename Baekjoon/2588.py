from sys import stdin

x = int(stdin.readline())
y = stdin.readline().rstrip()

for f in reversed(y):
    f = int(f)
    print(f*x)

print(int(x)*int(y))
