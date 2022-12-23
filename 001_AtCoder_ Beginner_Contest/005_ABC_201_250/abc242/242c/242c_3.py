"""
2022/12/10 12:14:27
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
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')        
sys.setrecursionlimit(500000)
INF = 10**17
MOD=998244353

N = II()
dp = [[0]*10 for _ in range(N)]
for i in range(1,10):
    dp[0][i] = 1
for n in range(1,N):
    for i in range(1,10):
        dp[n][i] += dp[n-1][i]
        if i - 1 >= 1:
            dp[n][i] += dp[n-1][i-1]
        if i + 1 <= 9:
            dp[n][i] += dp[n-1][i+1]
        dp[n][i] %= MOD

print(sum(dp[-1])%MOD)