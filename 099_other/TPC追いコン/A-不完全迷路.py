def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
from collections import deque

H, W = IIS()
E = [I() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if E[i][j] == 'S':
            start = (i, j)
        if E[i][j] == 'G':
            end = (i, j)

dist_s = [[-1] * W for _ in range(H)]
dist_e = [[-1] * W for _ in range(H)]
dist_s[start[0]][start[1]] = 0
dist_e[end[0]][end[1]] = 0

Q = deque()
Q.append(start)

done = [[False] * W for _ in range(H)]
while len(Q) > 0:
    i, j = Q.popleft()
    if done[i][j]:
        continue
    done[i][j] = True
    for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
        if 0<=(i+x)<H and 0<=(j+y)<W:
            if dist_s[x+i][y+j] != -1:
                dist_s[x+i][y+j] = min(dist_s[i][j] + 1, dist_s[x+i][y+j])
            else:
                dist_s[x + i][y + j] = dist_s[i][j] + 1
            if E[x+i][y+j] == '.':
                Q.append((i+x,j+y))

Q = deque()
Q.append(end)

done = [[False] * W for _ in range(H)]
while len(Q) > 0:
    i, j = Q.popleft()
    if done[i][j]:
        continue
    done[i][j] = True
    for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
        if 0<=(i+x)<H and 0<=(j+y)<W:
            if dist_e[x+i][y+j] != -1:
                dist_e[x+i][y+j] = min(dist_e[i][j] + 1, dist_e[x+i][y+j])
            else:
                dist_e[x + i][y + j] = dist_e[i][j] + 1
            if E[x+i][y+j] == '.':
                Q.append((i+x,j+y))
ans = -1
for i in range(H):
    for j in range(W):
        if E[i][j] == '#':
            if dist_e[i][j] != -1 and dist_s[i][j] != -1:
                ans = max(ans, dist_s[i][j] + dist_e[i][j])

print(ans)
