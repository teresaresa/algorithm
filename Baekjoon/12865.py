from sys import stdin

n, k = map(int, stdin.readline().split())
dp = [[0] * (k+1) for _ in range(n)]

items = list()
for i in range(n):
    items.append(list(map(int, stdin.readline().split())))

for i, item in enumerate(items):
    iw, iv = item

    for w in range(1, k+1):
        if w >= iw:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-iw] + iv)
        else:
            dp[i][w] = dp[i-1][w]

print(dp[-1][-1])
