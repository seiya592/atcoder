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

S = LLIIS(H)

#.の数を数える
cnt = 0
for line in S:
    for s in line:
        if s == '.':
            cnt += 1

Q = collections.deque()
Q.append((0,0))

dist = [[-1]*W for _ in range(H)]
dist[0][0] = 1
while len(Q) > 0:
    x,y = Q.popleft()
    for i,j in PLUS:
        if 0<=x+i<H and 0<=y+j<W:
            if dist[x+i][y+j] == -1 and S[x+i][y+j] != '#':
                dist[x+i][y+j] = dist[x][y]+1
                Q.append((x+i,y+j))

print(cnt - dist[H-1][W-1] if dist[H-1][W-1] != -1 else -1)

