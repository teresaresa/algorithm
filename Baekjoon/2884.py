#!/bin/python3
# https://www.acmicpc.net/problem/2884

time = str(input()).split(' ')
hours = int(time[0])
minutes = int(time[1])

set_minutes = minutes - 45
set_hours = hours

if minutes - 45 < 0:
    if hours == 0:
        hours = 24

    set_minutes = 60 + (minutes - 45)
    set_hours = hours - 1

print('{} {}'.format(set_hours, set_minutes))
