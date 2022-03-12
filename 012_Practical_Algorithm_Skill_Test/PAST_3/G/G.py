def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
from collections import deque
OFFSET = 201
N, X, Y = IIS()
B = [LIIS() for _ in range(N)]

b = [[True] * 403 for _ in range(404)]
dist = [[-1] * 403 for _ in range(404)]
Q = deque()
for x, y in B:
    b[x+OFFSET][y+OFFSET] = False

Q.append([OFFSET,OFFSET])
dist[OFFSET][OFFSET] = 0

while len(Q):
    x,y = Q.popleft()
    for i,j in [[x+1,y+1],[x,y+1],[x-1,y+1],[x+1,y],[x-1,y],[x,y-1]]:
        if not(0<=i<=OFFSET*2 and 0<=j<=OFFSET*2):
            continue
        elif dist[i][j] != -1:
            continue
        elif b[i][j]:
            Q.append([i,j])
            dist[i][j] = dist[x][y] + 1

print(dist[X+OFFSET][Y+OFFSET])