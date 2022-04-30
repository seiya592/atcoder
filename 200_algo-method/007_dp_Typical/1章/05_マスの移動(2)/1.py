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

dp = [10**10] * N
dp[0] = 0
# dp[1] = 0
for n in range(N):
    for i in range(n+1,min(n+M+1,N)):
        dp[i] = min(dp[n] + A[i] * (i-n),dp[i])
print(dp[N-1])