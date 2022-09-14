"""
2022/08/27 20:49:25
"""
import math


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
dp = [[0]*7 for _ in range(N)]
ans = 0
for k in range(N):
    for n in range(1,6+1):
        if k and math.floor(dp[k-1][0]) >= n:
            dp[k][n] = dp[k-1][0]
        else:
            dp[k][n] = n
    dp[k][0] = sum(dp[k]) / 6
print(dp[N-1][0])