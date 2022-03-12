def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(str, input().split()))

from collections import deque

R, C = IIS()
sy, sx = IIS()
gy, gx = IIS()
c = [I() for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

dist = [[-1] * C for _ in range(R)]
# dist = [[-1]*C]*R ←NG　配列のアドレスがコピーされる

Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

while len(Q) > 0:
    y, x = Q.popleft()
    for i, j in [[y-1, x], [y+1, x], [y, x-1], [y, x+1]]:
        if not(0 <= i < R) or not(0 <= j < C):
            continue
        elif dist[i][j] != -1:
            continue
        elif c[i][j] == '.':
            dist[i][j] = dist[y][x]+1
            Q.append([i,j])

print(dist[gy][gx])
