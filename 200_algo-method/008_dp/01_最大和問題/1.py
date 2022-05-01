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

dp = [0] * (N+1)

for n in range(N):
    dp[n+1] = max(dp[n],dp[n]+A[n])
print(dp[N])