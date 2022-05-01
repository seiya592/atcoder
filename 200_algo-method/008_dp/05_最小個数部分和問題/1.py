def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M = IIS()
A = LIIS()
dp = [[10**10] * (M+1) for _ in range(N+1)]
dp[0][0] = 0

for n in range(N):
    for i in range(M+1):
        dp[n+1][i] = min(dp[n+1][i], dp[n][i])

        if i + A[n] <= M:
            dp[n+1][i+A[n]] = min(dp[n+1][i+A[n]], dp[n][i] + 1)
print(dp[N][M] if dp[N][M] != 10**10 else -1)