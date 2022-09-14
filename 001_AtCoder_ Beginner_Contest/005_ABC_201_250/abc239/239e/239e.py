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


N, Q = IIS()
X = LIIS()
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

ans = [[] for _ in range(N+1)]

def dfs(n,o):
    t = [X[n-1]]
    for e in E[n]:
        if e == o:
            continue
        t.extend(dfs(e,n))
    t.sort(reverse=True)
    E[n] = t[:20]
    return E[n]
dfs(1,0)

for _ in range(Q):
    v,k = IIS()
    print(E[v][k-1])
