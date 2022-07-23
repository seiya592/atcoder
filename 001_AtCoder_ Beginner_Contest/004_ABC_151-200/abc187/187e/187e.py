import collections


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
AB = LLIIS(N-1)
Q = II()
E = [[] for _ in range(N+1)]
for a, b in AB:
    E[a].append(b)
    E[b].append(a)

deep = [-1] * (N+1)
deep[1] = 0
q = collections.deque()
q.append(1)
# 深さを求める
while q:
    n = q.popleft()
    for e in E[n]:
        if deep[e] != -1:
            continue
        deep[e] = deep[n] + 1
        q.append(e)

dp = [0] * (N+1)

for _ in range(Q):
    t,e,x = IIS()
    e -= 1
    if t == 1:
        now = AB[e][0]
        ng = AB[e][1]
    else:
        now = AB[e][1]
        ng = AB[e][0]

    if deep[now] > deep[ng]:
        dp[now] += x
    else:
        dp[ng] -= x
        dp[1] += x

q = collections.deque()
q.append(1)
done = [False] * (N+1)
while q:
    n = q.popleft()
    done[n] = True
    for e in E[n]:
        if done[e]:
            continue
        dp[e] += dp[n]
        q.append(e)

for d in dp[1:]:
    print(d)

# T[v][0] = 到達順　T[v][1] = 帰り順
# cnt = 0
# def dfs(now, last):
#     global cnt
#
#     T[now][0] = cnt
#     cnt += 1
#
#     for e in E[now]:
#         if last == e:
#             continue
#         dfs(e, now)
#
#     T[now][1] = cnt
#     cnt += 1
# dfs(1,0)
#
# dp = [0] * (N+1)
#
# for _ in range(Q):
#     t,e,x = IIS()
#     e -= 1
#     if t == 1:
#         now = AB[e][0]
#         ng = AB[e][1]
#     else:
#         now = AB[e][1]
#         ng = AB[e][0]
#
#     if T[now][0] > T[ng][0]:
#         dp[now] += x
#     else:
#         dp[ng] -= x
#         dp[1] += x
#
# def dfs2(now, last):
#     dp[now] += dp[last]
#     for e in E[now]:
#         if e == last:
#             continue
#         dfs2(e, now)
# dfs2(1, 0)
# for d in dp[1:]:
#     print(d)

# D = collections.defaultdict(int)
# #D[(from,now)] = fromからnowに着た時にnow含む子の頂点に足す値
# # nowからfromの場合 引いて全体に＋する
#
# for _ in range(Q):
#     t,e,x = IIS()
#     e -= 1
#     if t == 1:
#         D[(AB[e][1], AB[e][0])] += x
#     else:
#         D[(AB[e][0], AB[e][1])] += x
#
# E = [[] for _ in range(N+1)]
# for a, b in AB:
#     E[a].append(b)
#     E[b].append(a)
#
# ALL = 0
# dp = [0] * (N+1)
# def dfs(now, last):
#     global ALL
#     dp[now] += dp[last]
#     dp[now] += D[(last, now)]
#     dp[now] -= D[(now, last)]
#     ALL += D[(now, last)]
#
#     for e in E[now]:
#         if e == last:
#             continue
#         dfs(e, now)
#
# dfs(1, 0)
# for d in dp[1:]:
#     print(ALL + d)


# N = II()
# E = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     a,b = IIS()
#     E[a].append(b)
#     E[b].append(a)
#
# T = [[-1] * 2 for _ in range(N+1)]
# # T[v][0] = 到達順　T[v][1] = 帰り順
# cnt = 0
# def dfs(now, last):
#     global cnt
#
#     T[now][0] = cnt
#     cnt += 1
#
#     for e in E[now]:
#         if last == e:
#             continue
#         dfs(e, now)
#
#     T[now][1] = cnt
#     cnt += 1
#
# Q = II()
# F = [0] * (N*2+1)   #行き
# B = [0] * (N*2+1)   #帰り
#
# for _ in range(Q):
#     t, e, x =