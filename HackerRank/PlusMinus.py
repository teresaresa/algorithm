#!/bin/python3
# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    zero = 0
    positive = 0
    negative = 0
    
    for value in arr:
        if value == 0:
            zero += 1
        elif value > 0:
            positive += 1
        else:
            negative += 1
    
    length = len(arr)

    print(positive/length)
    print(negative/length)
    print(zero/length)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
