# def I(): return input().rstrip()
# def IS(): return input().split()
# def II(): return int(input())
# def IIS(): return map(int, input().split())
# def LIIS(): return list(map(int, input().split()))
# import sys
# sys.setrecursionlimit(10000000)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f

# N, M = IIS()
#
# E = [[] * N for _ in range(N)]
# for _ in range(M):
#     u, v, c = IIS()
#     u -= 1
#     v -= 1
#     E[u].append([v, c])
#     E[v].append([u, c])
#
# marked = [False] * N
# marked_count = N
#
# import heapq
# Q = []
# heapq.heapify(Q)
#
# for v, c in E[0]:
#     heapq.heappush(Q,(c,v,0))
#
# marked[0] = True
# marked_count -= 1
# ans = []
# while marked_count:
#     c, v , old = heapq.heappop(Q)
#     if marked[v]:
#         continue
#     ans.append([v,old,c])
#     marked[v] = True
#     marked_count -= 1
#
#     for next, c in E[v]:
#         heapq.heappush(Q, (c, next, v))


#プリム法で求めたedgeを使ってダイクストラ
# M = len(ans)
# V = [[] for _ in range(N)]
# for u,v,c in ans:
#     V[u].append([c,v])
#     V[v].append([c,u])
#
# cost = [-1] * N
# done = [False] * N
#
# Q = []
# heapq.heapify(Q)
# heapq.heappush(Q, (0,0))
# cost[0] = 0
#
# while len(Q) > 0:
#     c, i = heapq.heappop(Q)
#     if done[i]:
#         continue
#
#     done[i] = True
#
#     for c2, i2 in V[i]:
#
#         if cost[i2] == -1 or cost[i2] > cost[i] + c2:
#             cost[i2] = cost[i] + c2
#             heapq.heappush(Q,(cost[i2], i2))
# print(cost[1:])
#
# N, M = IIS()
#
# E = [[] * N for _ in range(N)]
# for i in range(M):
#     u, v, c = IIS()
#     u -= 1
#     v -= 1
#     E[u].append([v, c, i+1])
#     E[v].append([u, c, i+1])
#
# marked = [False] * N
# marked_count = N
#
# import heapq
# Q = []
# heapq.heapify(Q)
#
# for v, c, i in E[0]:
#     heapq.heappush(Q,(c,v,i))
#
# marked[0] = True
# marked_count -= 1
# ans = []
# while marked_count:
#     c, v , i = heapq.heappop(Q)
#     if marked[v]:
#         continue
#     ans.append(i)
#     marked[v] = True
#     marked_count -= 1
#
#     for next, c, i in E[v]:
#         heapq.heappush(Q, (c, next, i))
# print(*ans)

def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_d
import heapq

N, M = IIS()
V = [[] for _ in range(N)]
for i in range(M):
    u,v,c = IIS()
    u -= 1
    v -= 1
    V[u].append([c,v,i+1])
    V[v].append([c, u,i+1])

cost = [-1] * N
done = [False] * N

Q = []
heapq.heapify(Q)
heapq.heappush(Q, (0,0,0))
cost[0] = 0
ans = []
while len(Q) > 0:
    c, i, n = heapq.heappop(Q)
    if done[i]:
        continue

    done[i] = True
    ans.append(n)
    for c2, i2, n in V[i]:

        if cost[i2] == -1 or cost[i2] > cost[i] + c2:
            cost[i2] = cost[i] + c2
            heapq.heappush(Q,(cost[i2], i2, n))

# print(cost[N-1])
print(*ans[1:])

