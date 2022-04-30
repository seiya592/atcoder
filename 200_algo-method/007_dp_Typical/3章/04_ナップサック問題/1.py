def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M = IIS()
W = LIIS()
V = LIIS()

dp = [[0]*(M+1) for _ in range(N+1)]
for n in range(N):
    for w in range(M+1):
        dp[n+1][w] = max(dp[n+1][w],dp[n][w])
        if w + W[n] <= M:
            dp[n+1][w+W[n]] = max(dp[n+1][w+W[n]], dp[n][w]+V[n])
print(max(dp[N]))