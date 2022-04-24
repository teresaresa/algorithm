from sys import stdin

x = stdin.readline()
y = map(int, stdin.readline().split())

def sosu(int):
    for i in range(1, int):
        if int % i == 0 and i != 1:
            return False
    return True

cnt = 0
for i in y:
    if i > 1 and sosu(i):
        cnt += 1

print(cnt)
