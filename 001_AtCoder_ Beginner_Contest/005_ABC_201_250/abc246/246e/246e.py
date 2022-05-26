def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,1],[-1,1],[-1,-1],[1,-1]]
from collections import deque
import heapq
INF = 10**10
def check(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

#1h29m
#解説AC

N = II()
Ax,Ay = IIS()
Bx,By = IIS()
Ax -= 1
Ay -= 1
Bx -= 1
By -= 1
S = LLIIS(N)

Q = deque()

Q.append((-1,Ax,Ay))

dist = [[[INF]*4 for _ in range(N)] for _ in range(N)]
for i in range(4):
    dist[Ax][Ay][i] = 0
#x,y,向いている方向

while len(Q) > 0:
    m,x,y = Q.popleft()

    # if x == Bx and y == By: あってもなくても変わらない（20msくらい変わるかも）
    #     break
    for n, (i, j) in enumerate(PLUS):   #行先
        if check(x+i,y+j) and S[x+i][y+j] != '#':
            if m == n:
                if dist[x + i][y + j][n] > dist[x][y][m]:
                    dist[x+i][y+j][n] = dist[x][y][m]
                    Q.appendleft((n,x+i,y+j))
            else:
                if dist[x+i][y+j][n] > dist[x][y][m] + 1:
                    dist[x+i][y+j][n] = dist[x][y][m] + 1
                    Q.append((n,x + i, y + j))
print(min(dist[Bx][By]) if min(dist[Bx][By]) != INF else -1)

#拡張ダイクストラ 多分pythonでは無理
# Q = []
# heapq.heapify(Q)
#
# # 次の地点の距離, 向いている方向,x,y
#
# dist = [[[INF] * 5 for _ in range(N)] for _ in range(N)]
# #座標x,座標y,向き
# heapq.heappush(Q, (0, 4, Ax, Ay))
# dist[Ax][Ay][4] = 0
#
# done = [[False] * N for _ in range(N)]
#
# while len(Q) > 0:
#     d,m,x,y = heapq.heappop(Q)
#     if done[x][y]:
#         continue
#     done[x][y] = True
#
#     if x == Bx and y == By:
#         break
#
#     #次の行先
#     for n, (i, j) in enumerate(PLUS):
#         if check(x+i,y+j) and S[x+i][y+j] != '#':
#             if dist[x+i][y+j][n] > dist[x][y][m] + (m!=n):
#                 dist[x+i][y+j][n] = dist[x][y][m] + (m!=n)
#                 heapq.heappush(Q,(dist[x+i][y+j][n], n,x+i,y+j))
#
# print(min(dist[Bx][By]) if min(dist[Bx][By]) != INF else -1)


