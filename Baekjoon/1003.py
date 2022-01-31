from sys import stdin

zero = [1, 0, 1]
one = [0, 1, 1]

tc = int(stdin.readline())
for _ in range(tc):
    num = int(stdin.readline())

    if len(zero) <= num:
        for i in range(len(zero), num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])

    print(f'{zero[num]} {one[num]}')
