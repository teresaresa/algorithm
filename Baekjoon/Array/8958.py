from sys import stdin

tcc = int(stdin.readline())

for i in range(tcc):
    tc = stdin.readline()

    score = 0
    seq = 0
    for ox in tc:
        if ox == 'O':
            seq += 1
            score += seq
        else:
            seq = 0

    print(score)
