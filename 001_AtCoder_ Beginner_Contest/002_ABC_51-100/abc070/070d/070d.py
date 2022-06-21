def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(250000)
INF = 10**10


N = II()
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = IIS()
    E[a].append((b,c))
    E[b].append((a,c))

dist = [INF] * (N+1)

def dfs(n,m):
    """
    :param n:now
    :param m: old
    :return:
    """
    for e,c in E[n]:
        if e == m:
            continue
        dist[e] = dist[n] + c
        dfs(e,n)


Q,K = IIS()
dist[K] = 0
dfs(K,0)
for _ in range(Q):
    x,y = IIS()
    print(dist[x] + dist[y])
