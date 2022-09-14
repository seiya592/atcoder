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


N = II()
A = LIIS()

dp = [[0]*2 for _ in range(N+1)]
# dp[n番目に][０→勉強をしていない、１→勉強した]  = 実力
for n in range(N):
    dp[n+1][0] = max(dp[n][0], dp[n][1])
    dp[n+1][1] = dp[n][0] + A[n]
print(max(dp[-1]))