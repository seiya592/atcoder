import math


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


N = II()
XYP = LLIIS(N)

dist = [[INF] * N for _ in range(N)]



for i,(x,y,p) in enumerate(XYP):
    for j,(x,y,p) in enumerate(XYP):
        dist[i][j] = math.ceil((abs(XYP[i][0] - XYP[j][0]) + abs(XYP[i][1]- XYP[j][1])) / XYP[i][2])

for i in range(N):
    dist[i][i] = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            # form = math.ceil((abs(XYP[j][0] - XYP[i][0]) + abs(XYP[j][1]- XYP[i][1])) / XYP[j][2])
            # keiyu = math.ceil((abs(XYP[i][0] - XYP[k][0]) + abs(XYP[i][1]- XYP[k][1])) / XYP[i][2])
            dist[j][k] = min(dist[j][k], max(dist[j][i] , dist[i][k]))

ans = INF
for i in range(N):
    tmp = 0
    for j in range(N):
        tmp = max(tmp,dist[i][j])
    ans = min(ans,tmp)
print(ans)