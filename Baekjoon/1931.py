from sys import stdin

meet = int(stdin.readline())
schedule = list()

for _ in range(meet):
    schedule.append(list(map(int, stdin.readline().split())))

"""
1순위로 끝나는 시간을, 2순위로 시작하는 시간을 오름차순 정렬해야 함
sorted 랑 sort 랑 문법적 차이를 좀 찾아봐야 함

sorted(schedule, key=lambda x: (x[1], x[0]))
"""
schedule.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0
for time in schedule:
    if time[0] >= end_time:
        count += 1
        end_time = time[1]

print(count)
