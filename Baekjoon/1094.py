from sys import stdin

x = int(stdin.readline())
sticks = [64]

while True:
    if sum(sticks) > x:
        smallest = min(sticks)
        sticks.remove(smallest)

        half = int(smallest / 2)
        sticks.append(half)

        if sum(sticks) < x:
            sticks.append(half)

    if sum(sticks) == x:
        break

print(len(sticks))
