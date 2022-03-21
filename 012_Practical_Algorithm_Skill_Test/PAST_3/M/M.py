# def I(): return input().rstrip()
# def IS(): return input().split()
# def II(): return int(input())
# def IIS(): return map(int, input().split())
# def LIIS(): return list(map(int, input().split()))
#
# import sys
# from collections import deque
# # sys.setrecursionlimit(10000000)
#
# def has_bit(n, i):
#     return (n & (1 << i) > 0)
#
#
# N, M = IIS()
# E = [[] for _ in range(N+1)]
#
# for _ in range(M):
#     u, v = IIS()
#     E[u].append(v)
#     E[v].append(u)
#
# start = II()
# K = II()
# T = [start]
# T = T + LIIS()
#
# # 幅探索で最短経路を求める
#
# Q = deque()
# cost = [[0] * (N+1) for _ in range(N+1)]    #[start][end]の距離
# # cost[start][start] = 0
#
# for s in T:
#     Q.append(s)
#     while len(Q) > 0:
#         i = Q.popleft()
#         for j in E[i]:
#             if not cost[s][j]:
#                 cost[s][j] = cost[s][i] + 1
#                 Q.append(j)
#
# # 巡回セールスマン
# ALL = 2 ** K
# INF = 10**100
# dp = [[INF] * K for _ in range(ALL)]
#
# for i in range(K):
#     dp[1<<i][i] = cost[T[0]][T[i+1]]
#
#
#
# for n in range(ALL):
#     for i in range(K):
#         for j in range(K):
#             if has_bit(n,j) or i == j:
#                 continue
#             dp[n|1<<j][j] = min(dp[n|1<<j][j], dp[n][i] + cost[T[i+1]][T[j+1]])
#
# print(min(dp[ALL-1]))

from collections import deque
N, M = list(map(int,input().split()))
edges = []
for i in range(N):
    edges.append([])
for i in range(M):
    u, v = list(map(int,input().split()))
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

S = int(input())
S -= 1
K = int(input())
T = list(map(int,input().split()))
for i in range(K):
    T[i] -= 1

T.append(S)

Dist = []
for t1 in T:
    INF = 10 ** 100
    dist = [INF] * N
    que = deque()
    que.append(t1)
    dist[t1] = 0
    while len(que) > 0:
        i = que.popleft()
        for j in edges[i]:
            if dist[j] == INF:
                dist[j] = dist[i] + 1
                que.append(j)

    res = []
    for t2 in T:
        res.append(dist[t2])
    Dist.append(res)

ALL = 1<<K
cost = []
for n in range(ALL):
    cost.append([INF]*K)

for i in range(K):
    cost[1<<i][i] = Dist[K][i]

def has_bit(n,i):
    return (n & (1<<i) > 0)

for n in range(ALL):
    for i in range(K):
        for j in range(K):
            if has_bit(n, j) or i == j:
                continue
            cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + Dist[i][j])

print(min(cost[ALL-1]))
