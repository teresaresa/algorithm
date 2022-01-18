from sys import stdin

# https://www.acmicpc.net/problem/2775
testcase = int(stdin.readline())
for loop in range(testcase):
    k = int(stdin.readline())
    n = int(stdin.readline())

    f_map = [x for x in range(1, n+1)]
    for floor in range(k):
        for number in range(1, n):
            f_map[number] += f_map[number-1]

    print(f_map[-1])
