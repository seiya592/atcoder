def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, M = IIS()
C = LLIIS(N)

dp = [[10**10] * (M+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + C[i-1][j-1]
print(dp[N][M])