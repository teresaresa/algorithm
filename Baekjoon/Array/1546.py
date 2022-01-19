from sys import stdin


i = stdin.readline()
j = stdin.readline()

max = 0
for score in j.split():
    score = int(score)
    max = score if score > max else max

new_score = [int(score)/max*100 for score in j.split()]
print(sum(new_score)/float(i))
