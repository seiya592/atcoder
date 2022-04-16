def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, W = IIS()
WV = LLIIS(N)

#配るDP
dp = [[0] * (W+1) for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        wv = WV[i]
        # i番目の荷物を持ち帰らない
        dp[i+1][w] = max(dp[i][w], dp[i+1][w])
        # i番目の荷物を持ち帰る
        if w+wv[0] <= W:
            dp[i+1][w+wv[0]] = max(dp[i+1][w+wv[0]], dp[i][w] + wv[1])

print(max(dp[N]))