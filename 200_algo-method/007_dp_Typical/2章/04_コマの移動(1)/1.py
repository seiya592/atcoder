def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
dp = [[0] * N for _ in range(N)]
#配る
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i+1 < N:
            dp[i+1][j] += dp[i][j]
        if j+1 < N:
            dp[i][j+1] += dp[i][j]
print(dp[N-1][N-1])