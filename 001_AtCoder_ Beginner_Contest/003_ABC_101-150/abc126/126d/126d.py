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


N = II()
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v,w = IIS()
    E[u].append((v,w))
    E[v].append((u,w))

done = [False] *(N+1)
def dfs(n,c):
    done[n] = True
    color[n] = c

    for e,w in E[n]:
        if not done[e]:
            if w % 2 == 1:
                t =c^1
            else:
                t = c
            dfs(e,t)


color = [-1] * (N+1)

dfs(1,0)

for c in color[1:]:
    print(c)