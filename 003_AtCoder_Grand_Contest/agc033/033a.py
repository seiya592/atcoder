import collections


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]


H,W = IIS()

A = LLIIS(H)

Q = collections.deque()
dist = [[-1]*W for _ in range(H)]


for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            Q.append((i,j))
            dist[i][j] = 0

while len(Q) > 0:
    i,j = Q.popleft()

    for x,y in PLUS:
        if 0<=x+i<H and 0<=y+j<W and dist[x+i][y+j] == -1:
            dist[x + i][y + j] = dist[i][j] + 1
            Q.append((i+x,j+y))

ans = 0
for line in dist:
    ans = max(ans,max(line))
print(ans)