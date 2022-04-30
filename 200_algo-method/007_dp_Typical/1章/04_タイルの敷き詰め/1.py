def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
dp = [0] * (N+1)
dp[0] = 1

for n in range(N):
    dp[n+1] += dp[n]
    if N - 1 > n:
        dp[n+2] += dp[n]
    if N - 2 > n:
        dp[n+3] += dp[n]
print(dp[N])