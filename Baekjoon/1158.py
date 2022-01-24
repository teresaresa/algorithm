from sys import stdin

tc = list(map(int, stdin.readline().split()))
rmp = tc[1] - 1

people = [x for x in range(1, tc[0]+1)]

josephus = list()
index = 0
while len(people) != 0:
    index += rmp

    if index >= len(people):             # 이 부분 HELL
        index = index % len(people)

    josephus.append(people[index])
    people.pop(index)

print("<", ', '.join(str(i) for i in josephus), ">", sep="")
