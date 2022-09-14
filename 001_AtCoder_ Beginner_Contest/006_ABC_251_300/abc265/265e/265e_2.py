"""
2022/08/24 23:11:00
"""
import collections


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


N,M = IIS()
A,B,C,D,E,F = IIS()
MOD = 998244353
S = set()
for _ in range(M):
    x,y = IIS()
    S.add((x,y))

next = collections.Counter()
next[(0,0)] = 1
for _ in range(N):
    dp, next = next, collections.Counter()
    for (x,y),v in dp.items():
        for a,b in [(A,B),(C,D),(E,F)]:
            if (a+x,b+y) in S:
                continue
            next[(a+x,b+y)] += v % MOD

print(sum(next.values())%MOD)