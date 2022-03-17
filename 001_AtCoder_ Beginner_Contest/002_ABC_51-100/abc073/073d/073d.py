def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N,M,R = IIS()
r = LIIS()
INF = 10**100
dict = [[INF]*N for _ in range(N)]
for i in range(N):
    dict[i][i] = 0

for _ in range(M):
    a,b,c = IIS()
    dict[a-1][b-1] = c
    dict[b-1][a-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            dict[i][j] = min(dict[i][j], dict[i][k]+dict[k][j])

# ここまでで最短移動距離が求まる
def has_bit(n, i):
    return (n & (1<<i)) > 0

ALL = 2 ** R
cost = [[INF]*R for _ in range(ALL)]

cost[0][0] = 0
for i in range(1,R):
    cost[1<<i][i] = 0

for n in range(ALL):
    for i in range(R):
        for j in range(R):
            if has_bit(n,j) or i == j:
                continue
            cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + dict[r[i]-1][r[j]-1])

print(min(cost[ALL-1]))