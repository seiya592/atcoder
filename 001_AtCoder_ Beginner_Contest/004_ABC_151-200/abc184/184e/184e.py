"""
2022/10/21 18:43:58
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


H,W = IIS()
A = LI(H)

D = collections.defaultdict(list)

for i in range(H):
    for j in range(W):
        if A[i][j] == '.' or A[i][j] == '#':
            continue
        D[A[i][j]].append((i,j))

Q = collections.deque()
x,y = D['S'][0]
Q.append((x,y))
dist = [[INF] * W for _ in range(H)]
dist[x][y] = 0
while Q:
    x,y = Q.popleft()
    if A[x][y] == 'G':
        print(dist[x][y])
        exit()

    for i,j in PLUS(x,y):
        if 0<=i<H and 0<=j<W and A[i][j] != '#':
            if dist[i][j] > dist[x][y] + 1:
                dist[i][j] = dist[x][y] + 1
                Q.append((i,j))

    if 'a' <= A[x][y] <= 'z':
        for i, j in D[A[x][y]]:
            if dist[i][j] > dist[x][y] + 1:
                dist[i][j] = dist[x][y] + 1
                Q.append((i,j))
        D[A[x][y]] = [] # 2回目以降は探索しない

print(-1)