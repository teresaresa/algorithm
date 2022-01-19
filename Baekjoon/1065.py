from sys import stdin


# https://www.acmicpc.net/problem/1065 한수
def x(n):
    num_list = str(n)
    result = True

    for idx, num in enumerate(num_list):
        if idx == len(num_list)-1:
            break

        comp = int(num_list[idx+1]) - int(num)

        if idx == 0:
            diff = comp
            continue

        if comp != diff:
            result = False
            break

    return result


i = int(stdin.readline())
count = 0

for j in range(1, i+1):
    count += 1 if x(j) else 0

print(count)
