import bisect


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
P = LIIS()
for i,p in enumerate(P, start=2):
    E[p].append(i)

dist = [[0] for _ in range(N+1)]    # dist[n] = 距離がnの頂点の行きがけ順
FT = [[0]*2 for _ in range(N+1)]

now = 1

def dfs(n,d):
    global now
    FT[n][0] = now
    dist[d].append(now)
    now += 1

    for e in E[n]:
        dfs(e,d+1)

    FT[n][1] = now
    now += 1

dfs(1,0)

Q = II()
for _ in range(Q):
    u,d = IIS()
    t = dist[d]
    ans = bisect.bisect_right(t, FT[u][1]) - bisect.bisect_left(t, FT[u][0])
    print(ans)