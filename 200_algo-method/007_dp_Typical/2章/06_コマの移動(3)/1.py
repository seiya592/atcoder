def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
A = LLIIS(N)

dp = [[0] * N for _ in range(N)]
dp[0][0] = A[0][0]
for i in range(N):
    for j in range(N):
        if i + 1 < N:
            dp[i + 1][j] = max(dp[i][j] + A[i+1][j],dp[i+1][j])
        if j + 1 < N:
            dp[i][j + 1] = max(dp[i][j] + A[i][j+1],dp[i][j+1])
print(dp[N-1][N-1])