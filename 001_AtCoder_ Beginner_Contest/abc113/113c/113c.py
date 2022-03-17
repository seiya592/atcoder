def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()

import heapq
Q = [[] for _ in range(N+1)]

for i in range(N+1):
    heapq.heapify(Q[i])

for i in range(M):
    p, y = IIS()
    heapq.heappush(Q[p], (y,i))

ans = []
heapq.heapify(ans)
for i in range(1, N+1):
    if not Q[i]:
        continue

    city = 1
    while len(Q[i]) > 0:
        y, n = heapq.heappop(Q[i])
        tmp = str(i).zfill(6) + str(city).zfill(6)
        city += 1
        heapq.heappush(ans, (n,tmp))

while len(ans) > 0:
    n, a = heapq.heappop(ans)
    print(a)
