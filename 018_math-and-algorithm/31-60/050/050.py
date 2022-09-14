"""
2022/08/08 22:08:44
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

A,B = IIS()
ALL = math.ceil(math.log2(B)) + 1
MOD = 10**9+7

ans = 1
t = A
for i in range(ALL):
    if B & (1 << i):
        ans *= t
        ans %= MOD
    t *= t
    t %= MOD
print(ans)