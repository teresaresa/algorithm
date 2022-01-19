from sys import stdin

tcc = int(stdin.readline())

for i in range(tcc):
    tc = stdin.readline()
    tc = tc.split()

    div = int(tc[0])
    total = sum([int(tc[idx]) for idx in range(1, div+1)])
    avg = total/div

    cnt = 0
    for idx in range(1, div+1):
        if float(tc[idx]) > avg:
            cnt += 1

    print(f'{cnt/div*100:.3f}%')
