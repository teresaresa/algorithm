from sys import stdin
from itertools import permutations


tc = list(map(int, stdin.readline().split()))
num = [x for x in range(1, tc[0]+1)]

result = list(permutations(num, tc[1]))

for i in result:
    print(' '.join(str(e) for e in i))
