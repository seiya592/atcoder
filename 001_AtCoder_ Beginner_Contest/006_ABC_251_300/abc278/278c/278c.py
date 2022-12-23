"""
2022/11/19 20:55:52
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N,Q = IIS()

D = collections.defaultdict(set)

for _ in range(Q):
    t,a,b = IIS()
    if t == 1:
        D[a].add(b)
    if t == 2:
        if b in D[a]:
            D[a].remove(b)
    if t == 3:
        if b in D[a] and a in D[b]:
            print('Yes')
        else:
            print('No')
