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
# dp = [n種類目までの鍵を使って][開けれる箱をbitで表現] = 最低費用
ALL = 2 ** N
dp = [[INF]*ALL for _ in range(M+1)]
dp[0][0] = 0

for n in range(M):
    a,b = IIS()
    C = LIIS()
    t = 0
    for c in C:
        t += 2 ** (c-1)
    for i in range(ALL):
        dp[n+1][i] = min(dp[n+1][i], dp[n][i])
        dp[n+1][i|t] = min(dp[n+1][i|t], dp[n][i] + a)
print(dp[-1][-1] if dp[-1][-1] != INF else -1)