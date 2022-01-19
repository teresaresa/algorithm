import copy


# https://www.acmicpc.net/problem/4673
def d(n):
    n += sum([int(i) for i in str(n)])
    return n


n_list = [n for n in range(10000)]
sn_list = copy.deepcopy(n_list)

for n in n_list:
    if d(n) in sn_list:
        sn_list.remove(d(n))

for sn in sn_list:
    print(sn)
