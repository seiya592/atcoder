def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
import collections

# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e

H,W,N = IIS()

S = LLIIS(H)

Q = collections.deque()

for x in range(H):
    for y in range(W):
        if S[x][y] == 'S':
            next = (x,y)
            break
d = 0

for n in range(1,N+1):
    Q.append(next)
    dist = [[-1]*W for _ in range(W)]
    dist[next[0]][next[1]] = d
    while len(Q) > 0:
        x,y = Q.popleft()
        if S[x][y] == str(n):
            next = (x,y)
            d = dist[x][y]
            Q = collections.deque()
            break

        for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
            if 0<=x+i<H and 0<=y+j<W:
                if dist[x+i][y+j] == -1 and S[x+i][y+j] != 'X':
                    dist[x+i][y+j] = dist[x][y] + 1
                    Q.append((x+i,y+j))

print(d)