from sys import stdin

string = stdin.readline().rstrip()
length = len(string)
slice = 10


# 배열의 요소를 한 줄로 출력
def printing_one_line(arr):
    for s in arr:
        print(s, end="")
    print()


if length <= slice:
    printing_one_line(string)
else:
    loop = length // slice

    start, end = 0, 10
    for _ in range(loop):
        printing_one_line(string[start:end])

        start += slice
        end += slice

    if length % slice > 0:
        printing_one_line(string[start:end])
