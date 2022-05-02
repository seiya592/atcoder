def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


H,W = IIS()
X0,Y0,X1,Y1 = IIS()
S = LLIIS(H)

dist=[[10**10]*W for _ in range(H)]
dist[X0][Y0] = 0
done = [[False]*W for _ in range(H)]
from collections import deque

Q = deque()
Q.append((X0,Y0))
while len(Q) > 0:
    x,y = Q.popleft()
    if done[x][y]:
        continue
    done[x][y] = True
    for i,j in [[x+1,y], [x,y+1], [x-1,y], [x,y-1]]:
        if 0<=i<H and 0<=j<W and S[i][j] == 'W':
            dist[i][j] = min(dist[i][j], dist[x][y]+1)
            Q.append((i,j))
print(dist[X1][Y1])