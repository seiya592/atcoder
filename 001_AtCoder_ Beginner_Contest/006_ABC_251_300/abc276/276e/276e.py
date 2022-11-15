"""
2022/11/05 20:57:41
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17

# H, W = IIS()
# C = LI(H)



# for h in range(H):
#     for w in range(W):
#         if C[h][w] == 'S':
#             start = (h,w)
#
# done = [[0] * W for _ in range(H)]
# def dfs(i,j,d):
#     if C[i][j] == 'S' and d >= 4:
#         YES()
#     done[i][j] = 1
#
#
#     for x,y in PLUS(i,j):
#         if 0<=x<H and 0<=y<W and C[x][y] != '#' and not done[x][y]:
#             if C[x][y] == 'S' and d < 3:
#                 continue
#             dfs(x,y,d+1)
#     # done[i][j] = 0
#
# for x,y in PLUS(*start):
#     if 0<=x<H and 0<=y<W and C[x][y] != '#':
#         dfs(x,y,1)
# NO()



H, W = IIS()
C = LI(H)
for h in range(H):
    for w in range(W):
        if C[h][w] == 'S':
            start = (h,w)

Q = collections.deque()
dist = [[-1] * W for _ in range(H)]

for x,y in PLUS(*start):
    if 0<=x<H and 0<=y<W and C[x][y] != '#':
        # dist[x][y] = 1
        Q.append((x,y,0))

while Q:
    i,j,d = Q.popleft()
    dist[i][j] = d + 1
    # if dist[i][j] >= 0:
    #     continue
    if C[i][j] == 'S':
        YES()
    for x,y in PLUS(i,j):
        if 0 <= x < H and 0 <= y < W and C[x][y] != '#':
            if C[x][y] == 'S' and dist[i][j] < 3:
                #まだスタートにいけない
                continue
            if dist[x][y] >= 0:
                continue
            # dist[x][y] = dist[i][j] + 1
            Q.appendleft((x, y,d+1))
NO()