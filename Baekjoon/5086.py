from sys import stdin

result = list()
while True:
    tc = list(map(int, stdin.readline().split()))

    if tc == [0, 0]:
        break

    x = tc[0]
    y = tc[1]

    if x <= y:
        if y % x == 0:
            result.append("factor")
        else:
            result.append("neither")
    else:
        if x % y == 0:
            result.append("multiple")
        else:
            result.append("neither")

for _ in result:
    print(_)
