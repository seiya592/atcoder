"""
2022/09/03 20:35:25
"""
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
INF = 10**17


N,M = IIS()
A = LIIS()

dp = [[-INF] * (M+1) for _ in range(N+1)]
#dp[Nまでで][M個選んだ] ＝ 最大値
dp[0][0] = 0
for n in range(1,N+1):
    for i in range(M,-1,-1):
        dp[n][i] = max(dp[n-1][i],  dp[n][i])
        if i:
            dp[n][i] = max(dp[n][i], dp[n-1][i-1] + A[n-1] * i)

ans = -INF
for d in dp:
    ans = max(ans,d[-1])
print(ans)
