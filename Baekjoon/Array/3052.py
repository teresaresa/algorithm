from sys import stdin


div = 42
rl = list()
for i in range(10):
    j = int(stdin.readline())
    if j % div not in rl:
        rl.append(j % div)

print(len(rl))
