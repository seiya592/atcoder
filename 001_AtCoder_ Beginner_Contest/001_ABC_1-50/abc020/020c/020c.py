import heapq


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


H,W,T = IIS()
S = LI(H)

for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            start = (i,j)
        if S[i][j] == 'G':
            goal = (i,j)

def calc(X):
    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q,(0,*start))

    dist = [[-1] * W for _ in range(H)]

    while Q:
        d, x, y = heapq.heappop(Q)
        if dist[x][y] != -1:
            continue
        dist[x][y] = d
        for i,j in PLUS(x,y):
            if 0<=i<H and 0<=j<W:
                if dist[i][j] == -1:
                    nextd = d+1 if S[i][j] != '#' else d+X
                    heapq.heappush(Q,(nextd, i,j))

    if T >= dist[goal[0]][goal[1]]:
        return True
    return False


ok = 0
ng = INF
while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if calc(mid):
        ok = mid
    else:
        ng = mid

print(ok)