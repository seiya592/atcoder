def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20


N,K = IIS()
A = LIIS()

dp = [[0] * (K+1+1) for _ in range(N+1)]
# dp[n人目までで][k個の飴を配った時の] = 組み合わせ数

# 愚直に書いた場合
# dp[0][0] = 1
# for n in range(1,N+1):
#     for i in range(K+1):
#         for j in range(A[n-1]+1):
#             if i - j >= 0:  #配れるとき
#                 dp[n][i] += dp[n-1][i-j]
# pass


dp[0][1] = 1
for n in range(1,N+1):
    for i in range(1,K+1+1):
        MIN = max(0,i-A[n-1]-1)
        dp[n][i] = dp[n-1][i] - dp[n-1][MIN]
        dp[n][i] += dp[n][i-1]
        dp[n][i] %= 10**9+7



pass
print(dp[N][K+1])

