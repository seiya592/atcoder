import collections
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
sys.setrecursionlimit(100000)
INF = 10**9


H,W = IIS()
START = list(IIS())
GOAL = list(IIS())
S = LI(H)

Q = collections.deque()
dist = [[[INF]*4 for _ in range(W)] for _ in range(H)]
for i in range(4):
    Q.append((START[0]-1,START[1]-1,i))
    dist[START[0]-1][START[1]-1][i] = 0

dx = (1,0,-1,0)
dy = (0,1,0,-1)

while len(Q):
    x,y,m = Q.popleft() # m = 向いている方向
    # 向いている方向に歩く

    i,j = dx[m]+x, dy[m]+y

    if 0<=i<H and 0<=j<W and S[i][j] != '#':    #向いている方向に1歩進めるか？
        for n in range(4):  #移動した後に向きを変える
            cost = dist[x][y][m] + (0 if n==m else 1)
            if dist[i][j][n] > cost:
                dist[i][j][n] = cost
                Q.appendleft((i, j, n)) if n == m else Q.append((i,j,n))
                # if n == m:
                #     Q.appendleft((i,j,n))
                # else:
                #     Q.append((i,j,n))
print(min(dist[GOAL[0]-1][GOAL[1]-1]))
