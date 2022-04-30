def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)

N = II()
A = LIIS()

dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[0][i] = A[i]

for i in range(1,N):
    for j in range(N):
        for k in range(max(0,j-1),min(N,j+2)):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= 100
print(dp[N-1][N-1])