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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N,M = IIS()
E = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)


def bsf(n):
    Q = collections.deque()
    Q.append(n)
    dist = [INF] * (N+1)
    dist[n] = 0
    while Q:
        n = Q.popleft()

        if n != 0:
            for e in E[n]:
                if dist[e] != INF:
                    continue
                dist[e] = dist[n]+1
                Q.append(e)
    return dist


S = bsf(1)
G = bsf(N)

ans = []
for i in range(1,N+1):
    t = min(S[N], S[0]+G[i], S[i]+G[0], S[0]+G[0])
    if t >= INF:
        ans.append(-1)
    else:
        ans.append(t)
print(*ans)
