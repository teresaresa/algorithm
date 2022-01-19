from sys import stdin


# https://www.acmicpc.net/problem/10872 재귀
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(int(stdin.readline())))
