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


N,M = IIS()
E = [[] for _ in range(N+1)]
EE = [[] for _ in range(N+1)]
for _ in range(M):
    l,r,d = IIS()
    E[l].append((r,d))
    EE[r].append((l,d))


def dfs(n):

    for e, d in E[n]:
        if done[e]:
           if dist[e] != dist[n] + d:
                print('No')
                exit()
        else:
            dist[e] = dist[n] + d
            done[e] = True
            dfs(e)

    for e, d in EE[n]:
        if done[e]:
            if dist[e] != dist[n] - d:
                print('No')
                exit()
        else:
            dist[e] = dist[n] - d
            done[e] = True
            dfs(e)


done = [False] * (N+1)
dist = [0] * (N+1)
for i in range(1,N+1):
    if not done[i]:
        dfs(i)

print('Yes')