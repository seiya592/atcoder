"""
2022/10/18 17:51:06
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N = II()
PA = LLIIS(N)

dp = [[0] * (N+1) for _ in range(N+1)]
#配る
for l in range(N+1):
    for r in range(N,l,-1):
        #左を消す
        p,a = PA[l]
        dp[l+1][r] = max(dp[l+1][r], dp[l][r] + (a if l < p <= r else 0))

        #右を消す
        p,a = PA[r-1]
        dp[l][r-1] = max(dp[l][r-1], dp[l][r] + (a if l < p <= r else 0))
ans = 0
for i in range(1,N+1):
    ans = max(ans, dp[i][i])
print(ans)