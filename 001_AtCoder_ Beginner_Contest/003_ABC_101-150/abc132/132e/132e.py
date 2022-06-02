import collections


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20


N, M = IIS()
dist = [[INF] * 3 for _ in range(N+1)]
E = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = IIS()
    E[u].append(v)

S,T = IIS()

Q = collections.deque()
Q.append((S,0))
dist[S][0] = 0

while Q:
    n,c = Q.popleft()

    for e in E[n]:
        cost = (1 if c == 2 else 0)
        next = (c+1)%3
        if dist[n][c] + cost <  dist[e][next]:
            dist[e][next] = dist[n][c] + cost
            Q.append((e,next))
print(dist[T][0] if dist[T][0] != INF else -1)
