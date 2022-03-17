def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N,M, = IIS()
INF = 10**100
cost = [[INF]*N for _ in range(N)]
ABC = [LIIS() for _ in range(M)]
for a, b, c in ABC:
    cost[a-1][b-1] = c
    cost[b-1][a-1] = c

#各点-点の最短距離算出
for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# いらない辺を数える
ans = 0
for a, b, c in ABC:
    flg = False
    for i in range(N):
        if cost[a-1][i] + cost[i][b-1] <= c:    # 迂回で対象の辺以下のコストなら
            flg = True
            break
    if flg:
        ans += 1

print(ans)
