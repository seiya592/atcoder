"""
2022/10/27 18:11:26
"""
import heapq


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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N,M,T = IIS()
A = LIIS()

E = [[] for _ in range(N+1)]
R = [[] for _ in range(N+1)]    #逆方向に辺を張る

for _ in range(M):
    a,b,c = IIS()
    E[a].append((b,c))
    R[b].append((a,c))


def calc(edge):
    Q = []
    heapq.heapify(Q)

    dist = [INF] * (N+1)
    heapq.heappush(Q,(0,1))
    while Q:
        d,n = heapq.heappop(Q)
        if dist[n] <= d:
            continue
        dist[n] = d

        for e, k in edge[n]:
            heapq.heappush(Q,(k+d, e))

    return dist

to = calc(E)
fr = calc(R)

ans = 0
for a,t,f in zip(A,to[1:], fr[1:]):
    ans = max(ans,a * (T-(t+f)))
print(ans)