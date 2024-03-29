import bisect


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]

import sys
sys.setrecursionlimit(100000)
INF = 10**20


N = II()
W = []
for _ in range(N):
    W.append(II())

ans = [-1]
for w in W:
    if ans[-1] < w:
        ans.append(w)
    else:
        ans[bisect.bisect_left(ans, w)] = w
print(len(ans)-1)