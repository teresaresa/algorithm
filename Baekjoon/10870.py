from sys import stdin


# https://www.acmicpc.net/problem/10870 재귀
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(int(stdin.readline())))
