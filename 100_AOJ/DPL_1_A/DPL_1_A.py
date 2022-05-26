def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]
INF = 10**20


N,M = IIS()
C = LIIS()

dp = [[INF] * (N+1) for _ in range(M+1)]
dp[0][0] = 0
# もらう
for n in range(1,M+1):
    for i in range(N+1):
        # 使わない
        dp[n][i] = min(dp[n][i], dp[n-1][i])

        # 使う
        if i - C[n-1] >= 0:
            dp[n][i] = min(dp[n][i], dp[n][i-C[n-1]] + 1)
print(dp[M][N])