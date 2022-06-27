import bisect
import collections
import queue


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


N = II()
P = LIIS()
Q = II()
UD = LLIIS(Q)

IO = [[-1,-1] for _ in range(N+1)]

E = [[] for _ in range(N+1)]
for i, p in enumerate(P,start=2):
    E[p].append(i)


INs = [[] for _ in range(N)]
cnt = 0
def dfs(n,d):
    global cnt
    IO[n][0] = cnt
    INs[d].append(cnt)
    cnt += 1


    for e in E[n]:
        dfs(e,d+1)

    IO[n][1] = cnt
    cnt += 1
dfs(1,0)

for u,d in UD:
    i,o = IO[u]
    print(bisect.bisect_left(INs[d], o) - bisect.bisect_left(INs[d],i))





# N = II()
# P = LIIS()
# Qi = II()
# E = [[] for _ in range(N+1)]
# UD = LLIIS(Qi)
# for i, p in enumerate(P,start=2):
#     E[p].append(i)
#
# D = [[] for _ in range(N)]
# for u, d in UD:
#     D[d].append(u)
#
# Q = collections.deque()
# Q.append((1,0))
#
# dist = [-1] * (N+1)
# ans = [[0]*N for _ in range(N+1)]
# cnt = [0] * (N+1)
# now = 0
# while Q:
#     n,d = Q.popleft()
#
#     if now != d:
#         # 深さが１つ上がったら過去の深さを清算する
#         for i in D[now]:
#             if dist[i] != -1:
#                 # 過去に通ったことあるなら含まれている
#                 if dist[i] == now:
#                     # 同じ階層なら１つだけ
#                     ans[i][now] += 1
#                 else:
#                     #上の階層ならこの階層の分だけ
#                     ans[i][now] += cnt[now]
#         now += 1
#
#     dist[n] = d
#
#     for e in E[n]:
#         Q.append((e,d+1))
#
#     cnt[d] += 1
# else:
#     # 最後の深さを清算する
#     for i in D[now]:
#         if dist[i] != -1:
#             # 過去に通ったことあるなら含まれている
#             if dist[i] == now:
#                 # 同じ階層なら１つだけ
#                 ans[i][now] += 1
#             else:
#                 # 上の階層ならこの階層の分だけ
#                 ans[i][now] += cnt[now]
#
# for u, d in UD:
#     print(ans[u][d])

