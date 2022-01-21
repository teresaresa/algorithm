from sys import stdin
from itertools import combinations

maximum = list(map(int, stdin.readline().split()))[-1]
cards = list(map(int, stdin.readline().split()))
result = 0

for card in combinations(cards, 3):
    if result < sum(card) <= maximum:
        result = sum(card)

print(result)
