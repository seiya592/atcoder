def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,W = IIS()
WV = LLIIS(N)

dp = [[0]*(W+1) for _ in range(N+1)]

for n in range(N):
    for w in range(W+1):
        dp[n+1][w] = max(dp[n][w], dp[n+1][w])
        if w + WV[n][0] <= W:
            dp[n+1][w+WV[n][0]] = max(dp[n+1][w+WV[n][0]], dp[n][w] + WV[n][1])
print(dp[N][W])