"""
2022/08/09 20:22:27
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


N, K = IIS()
A = LIIS()

ALL = math.ceil(math.log2(K)) + 1
dp = [[0] * (N+1) for _ in range(ALL+1)]

for i,a in enumerate(A,start=1):
    dp[0][i] = a

for n in range(ALL):
    for i in range(N+1):
        dp[n+1][i] = dp[n][dp[n][i]]

now = 1
for i in range(ALL+1):
    if K & (1<<i):
        now = dp[i][now]
print(now)