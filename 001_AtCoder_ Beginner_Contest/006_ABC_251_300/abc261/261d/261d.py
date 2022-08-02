def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, M = IIS()
X = LIIS()
BONUS = [0] * (N+1)
for _ in range(M):
    c,y = IIS()
    BONUS[c] += y

# dp[i回目のトス][n連続ボーナス継続中]
dp = [[-INF] * (N+1) for _ in range(N+1)]
dp[0][0] = 0
for n in range(N):
    for i in range(N):
        if dp[n][i] == -INF:
            continue
        #裏
        dp[n+1][0] = max(dp[n+1][0], dp[n][i])

        #表
        dp[n+1][i+1] = max(dp[n+1][i+1], dp[n][i]+X[n]+BONUS[i+1])
print(max(dp[-1]))