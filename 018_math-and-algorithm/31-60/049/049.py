"""
2022/08/08 21:45:20
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
dp = [0] * (N+1)

dp[1] = 1
dp[2] = 1
MOD = 10**9+7
for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= MOD
print(dp[N])