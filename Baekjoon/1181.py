from sys import stdin

tc = int(stdin.readline())
words = list()
for _ in range(tc):
    word = stdin.readline().rstrip()
    if (word, len(word)) not in words:
        words.append((word, len(word)))

words = tuple(words)
words = sorted(words, key=lambda x: (x[1], x[0]))

for result in words:
    print(result[0])
