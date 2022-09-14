"""
2022/08/09 22:49:36
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


# 最大でもB以下にしかならない
A,B = IIS()
def calc(n):
    a = math.ceil(A/n)
    b = math.floor(B/n)
    return b-a >= 1

for i in range(1,B+1):
    if calc(i):
        ans = i
print(ans)