from sys import stdin

# https://www.acmicpc.net/problem/1100
count = 0
for i in range(8):
    board = stdin.readline().rstrip()
    for j in range(8):
        if (i % 2 == j % 2) and board[j] == 'F':
            count += 1

print(count)
