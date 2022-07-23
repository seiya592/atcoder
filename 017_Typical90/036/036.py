def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, Q = IIS()

XY = LLIIS(N)
UV = []
for x,y in XY:
    UV.append([x-y, x+y])

Xmax = max([u for u, _ in UV])
Xmin = min([u for u ,_ in UV])
Ymax = max([v for _, v in UV])
Ymin = min([v for _, v in UV])

for _ in range(Q):
    q = II() - 1
    print(max(abs(UV[q][0] - Xmax), abs(UV[q][0] - Xmin), abs(UV[q][1] - Ymax), abs(UV[q][1] - Ymin)))
