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
for _ in range(M):
    u,v,c = IIS()
    V[u].append([c,v])

cost = [-1] * N
done = [False] * N

Q = []
heapq.heapify(Q)
heapq.heappush(Q, (0,0))
cost[0] = 0

while len(Q) > 0:
    c, i = heapq.heappop(Q)
    if done[i]:
        continue

    done[i] = True

    for c2, i2 in V[i]:

        if cost[i2] == -1 or cost[i2] > cost[i] + c2:
            cost[i2] = cost[i] + c2
            heapq.heappush(Q,(cost[i2], i2))

print(cost[N-1])

