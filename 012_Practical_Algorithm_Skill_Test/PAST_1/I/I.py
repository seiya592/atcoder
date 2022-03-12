def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()
S = []
C = []
ALL = 2 ** N

for i in range(M):
    s, c = IS()

    y_bit = 0
    for j in range(len(s)):
        if s[j] == 'Y':
            y_bit += 1 << j
    S.append(y_bit)
    C.append(int(c))
INF = 10 ** 100

cost = [[INF] * (ALL + 1) for _ in range(M+1)]
cost[0][0] = 0


for i in range(1,M+1):
    for j in range(ALL):
        cost[i][j] = min(cost[i][j], cost[i-1][j])  # 変化なし
        cost[i][j|S[i-1]] = min(cost[i][j|S[i-1]], cost[i-1][j]+C[i-1])

ans = cost[M][ALL-1]
if ans == INF:
    print(-1)
else:
    print(ans)