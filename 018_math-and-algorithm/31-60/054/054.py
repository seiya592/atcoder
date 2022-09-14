"""
2022/08/09 18:44:27
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
MOD = 10**9


def calc(a,b):
    #二乗
    ans = [[0,0],[0,0]]

    for i in range(2):
        for k in range(2):
            for j in range(2):
                ans[i][j] += a[i][k] * b[k][j]
                ans[i][j] %= MOD
    return ans

N = II()-2
ALL = math.ceil(math.log2(N))+1


a = [[1,1],[1,0]]
ans = [[1,1],[1,0]]
for i in range(ALL):

    if N & (1 << i):
        ans = calc(ans, a)
    a = calc(a,a)

print((ans[1][0] + ans[1][1])%MOD)