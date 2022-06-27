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
sys.setrecursionlimit(500000)
INF = 10**10

#下が通るか考える
#in
# 10 2
# 0 1
# 0 10

# out
# 1 2 2 2 2 2 2 2 2 1

N,M = IIS()
E = [[] for _ in range(N+1)]
#頂点0 = テレポートとする
for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

def bfs(n):
    dist = [INF] * (N+1)
    dist[n] = 0
    Q = collections.deque()
    Q.append(n)

    while Q:
        f = Q.popleft()
        if f == 0:
            continue

        for e in E[f]:
            if dist[e] != INF:
                continue
            dist[e] = dist[f] + 1
            Q.append(e)
    return dist

fr = bfs(1)
to = bfs(N)


ans = []
for i in range(1,N+1):
    t = min(fr[N], fr[0]+to[i], fr[i]+to[0], fr[0]+to[0])
    ans.append(t if t != INF else -1)
print(*ans)

