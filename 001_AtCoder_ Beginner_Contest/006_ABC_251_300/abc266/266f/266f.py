"""
2022/08/27 20:49:30
"""
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


N = II()
E = [[] for _ in range(N+1)]
for _ in range(N):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

S = [-1] * (N+1)
G = [-1] * (N+1)
done = [False] * (N+1)
dist = [-1] * (N+1)
dist[1] = 0
cnt = 0

def dfs(n):
    done[n] = True

    global cnt
    S[n] = cnt
    cnt += 1

    for e in E[n]:
        if done[e]:
            continue
        dist[e] = dist[n]+1
        dfs(e)
    G[n] = cnt
    cnt += 1

dfs(6)

Q = II()

for _ in range(Q):
    x,y = IIS()
    t = abs(dist[x]-dist[y])
    if abs(S[x] - S[y]) == t or abs(G[x]-G[y]) == t:
        print('Yes')
    else:
        print('No')