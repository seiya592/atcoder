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
INF = 10**10
import math


N,K = IIS()
A = LIIS()

XY = LLIIS(N)

dist = [INF] * N

for i in range(N):
    for j in range(N):
        if i+1 in A:
            dist[j] = min(math.sqrt(abs(XY[i][0]-XY[j][0]) ** 2 + abs(XY[i][1]-XY[j][1]) ** 2),dist[j])
print(max(dist))