def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_e

N, M = IIS()
INF = 10**100

cost = [[INF] * N for _ in range(N)]
for _ in range(M):
    u, v, c = IIS()
    cost[u][v] = c
for i in range(N):
    cost[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

ans = 0
for c in cost:
    ans += sum(c)

print(ans)