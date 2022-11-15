"""
2022/09/15 18:40:20
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

N, M = IIS()
H = [0]+LIIS()
E = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = IIS()
    if H[u] > H[v]:
        E[u].append((0,v))
        E[v].append((H[u]-H[v], u))
    else:
        E[v].append((0, u))
        E[u].append((H[v] - H[u], v))

Q = []
heapq.heapify(Q)
dist = [INF] * (N+1)
dist[0] = 0
heapq.heappush(Q,(0,1))

while Q:
    d,n = heapq.heappop(Q)
    if dist[n] <= d:
        continue

    dist[n] = d

    for v, e in E[n]:
        heapq.heappush(Q,(v+dist[n], e))

ans = []
for d,h in zip(dist[1:],H[1:]):
    ans.append(H[1]-h-d)
print(max(ans))


# N, M = IIS()
# H = LIIS()
# H = [H[0]] + H
# E = [[] for _ in range(N+1)]
# for _ in range(M):
#     u,v = IIS()
#     E[u].append(v)
#     E[v].append(u)
#
# Q = []
# heapq.heapify(Q)
#
# val = [-INF] * (N+1)
# val[0] = 0
#
# heapq.heappush(Q, (0, 1))
#
# while Q:
#     d, n = heapq.heappop(Q)
#     d = -d
#     if d <= val[n]:
#         continue
#
#     val[n] = d
#
#     for e in E[n]:
#         # コストを算出
#         if H[n] > H[e]:
#             v = -(abs(H[n]-H[e]) + val[n])
#         elif H[n] < H[e]:
#             v = -(abs(H[n]-H[e])*-2 + val[n])
#         else:
#             v = -val[n]
#
#         if val[e] < -v:
#             heapq.heappush(Q,(v,e))
#
# print(max(val))