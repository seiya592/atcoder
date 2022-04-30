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

dp = [[0] * 3 for _ in range(N+1)]
#もらう
for n in range(1,N+1):
    for k in range(3):
        dp[n][k] = max(dp[n][k], dp[n-1][(k+1)%3] + A[n-1][k], dp[n-1][(k+2)%3] + A[n-1][k])
print(max(dp[N]))