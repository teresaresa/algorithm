from sys import stdin

# 1158 풀고 두 번째 도전 => 여전히 어렵다 윽
n, k = map(int, stdin.readline().split())
people = [x for x in range(1, n+1)]

josephus = list()
index, k = 0, k-1
while len(people) > 0:
    index += k

    if index >= len(people):
        index = index % len(people)

    josephus.append(people[index])
    people.pop(index)

print('<', ', '.join(str(i) for i in josephus), '>', sep='')
