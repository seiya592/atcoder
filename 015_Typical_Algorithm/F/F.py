def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f

N, M = IIS()

E = [[] * N for _ in range(N)]
for _ in range(M):
    u, v, c = IIS()
    E[u].append([v, c])
    E[v].append([u, c])

marked = [False] * N
marked_count = N

import heapq
Q = []
heapq.heapify(Q)

for v, c in E[0]:
    heapq.heappush(Q,(c,v))

marked[0] = True
marked_count -= 1
ans = 0
while marked_count:
    c, v = heapq.heappop(Q)
    if marked[v]:
        continue
    ans += c
    marked[v] = True
    marked_count -= 1

    for v, c in E[v]:
        heapq.heappush(Q, (c, v))

print(ans)
