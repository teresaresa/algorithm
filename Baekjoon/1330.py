#!/bin/python3
# https://www.acmicpc.net/problem/1330

comparison = str(input()).split(' ')
if int(comparison[0]) > int(comparison[1]):
    print('>')
elif int(comparison[0]) == int(comparison[1]):
    print('==')
else:
    print('<')
