import collections
import queue


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


H,W = IIS()
S = LI(H)

Q = collections.deque()
SG = []
for i,s in enumerate(S):
    for j,ss in enumerate(s):
        if ss == 'o':
            SG.append((i,j))

ans = abs(SG[0][0] - SG[1][0]) + abs(SG[1][1]-SG[0][1])
print(ans)