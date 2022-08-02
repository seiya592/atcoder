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
XY = LLIIS(N)
ans = INF
for i in range(N):
    x,y = XY[i]
    for j in range(i+1,N):
        a,b = XY[j]

        ans = min(ans, math.sqrt((x-a)**2 + (y-b)**2))
print(ans)