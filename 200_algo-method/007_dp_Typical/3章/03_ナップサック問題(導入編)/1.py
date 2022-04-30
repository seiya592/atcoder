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
B = LIIS()

dp = [[-1] * (M) for _ in range(N)]
dp[0][0] = 0
for n in range(N-1):
    for m in range(M):
        dp[n+1][m] = max(dp[n+1][m], dp[n][m])
        if m + A[n] < M and dp[n][m] != -1:
            dp[n+1][m+A[n]] = max(dp[n+1][m+A[n]],dp[n][m] + B[n])
print(dp[N-1][M-1])