"""
2022/08/08 20:19:28
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


H, W = IIS()
sx, sy = IIS()
gx, gy = IIS()

C = LI(H)

Q = collections.deque()
Q.append((sx-1,sy-1))

dist = [[-1] * W for _ in range(H)]
dist[sx-1][sy-1] = 0

while Q:
    a,b = Q.popleft()

    for x,y in PLUS(a,b):
        if 0<=x<H and 0<=y<W:
            if C[x][y] == '#':
                continue
            if dist[x][y] > -1:
                continue
            dist[x][y] = dist[a][b] + 1
            Q.append((x,y))
print(dist[gx-1][gy-1])