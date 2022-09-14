"""
2022/09/07 17:34:54
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
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N,M = IIS()
E = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = IIS()
    E[a].append((b,c))

def calc(n):
    dist = [INF] * (N+1)    # 要素0をn to nとする
    done = [False] * (N+1)

    Q = []
    heapq.heapify(Q)

    for e, d in E[n]:
        if e == n:
            # n to nの辺をチェック
            dist[0] = min(dist[0], d)

    dist[n] = 0

    heapq.heappush(Q, (0, n))

    cnt = N - 1
    while Q and cnt:
        c, v = heapq.heappop(Q)
        if done[v]:
            continue


        for e,d in E[v]:
            if done[e]:
                continue
            if dist[e] > dist[v] + d:
                dist[e] = dist[v] + d
                heapq.heappush(Q, (dist[e],e))
        done[v] = True
        cnt -= 1

    return dist

ans = [[] for _ in range(N+1)]

for n in range(1,N+1):
    ans[n] = calc(n)

for i in range(1,N+1):
    t = INF
    for j in range(1,N+1):
        if i == j:
            t = min(t, ans[i][0])
        else:
            t = min(t, ans[i][j]+ans[j][i])
    print(t if t != INF else -1)
