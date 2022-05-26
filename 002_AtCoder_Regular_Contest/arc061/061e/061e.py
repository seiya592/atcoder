import collections


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]
INF = 10**10

# N,M = IIS()
# E = [[] for _ in range(N+1)]
#
# for _ in range(M):
#     p,q,c = IIS()
#     E[p].append((q,c))
#     E[q].append((p,c))
#
#
# Q = collections.deque()
# dist = [[INF] * (N+1) for _ in range(10**6+1)]
# # done = [[False] * (N+1) for _ in range(10**6+1)]
# dist[0][1] = 0
#
# # for e in E[1]:
# #     Q.append((e[0],e[1],1))
# #     dist[e[0]] = dist[1] + (0 != e[1])
# #Q = 次の行先、次の行先の会社、現在の地点
#
#
# Q.append((1,0))
# #Q = 次の行先、次の行先に行くための会社
#
# while len(Q) > 0:
#     n,c = Q.popleft()
#     # if done[c][n]:
#     #     continue
#     # done[c][n] = True
#     if n == N:
#         print(dist[c][n])
#         exit()
#
#     for v,e in E[n]:
#         if c == e:
#             # 同じ会社
#             if dist[e][v] > dist[c][n]:
#                 dist[e][v] = dist[c][n]
#                 Q.appendleft((v,e))
#         else:
#             if dist[e][v] > dist[c][n] + 1:
#                 dist[e][v] = dist[c][n] + 1
#                 Q.append((v,e))
# print(-1)
# ans = 10**10
# for d in dist:
#     ans = min(ans,d[N])
#
# print(dist[N] if dist[N] != INF else -1)