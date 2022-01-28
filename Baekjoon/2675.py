from sys import stdin

tc = int(stdin.readline())
for _ in range(tc):
    num, word = stdin.readline().split()
    for w in word:
        print(w * int(num), end="")
    print()
