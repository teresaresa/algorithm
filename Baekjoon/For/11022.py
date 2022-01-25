from sys import stdin

n = int(stdin.readline())
for case in range(1, n+1):
    num_list = list(map(int, stdin.readline().split()))

    print(f'Case #{case}: {num_list[0]} + {num_list[1]} = {sum(num_list)}')
