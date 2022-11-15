"""
2022/10/17 19:28:57
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


#ふつうにDPでやる

N,S = IIS()
A = LIIS()
dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1

# もらう
for n in range(1,N+1):
    for i in range(S+1):
        dp[n][i] += dp[n-1][i]
        if i - A[n-1] >= 0:
            dp[n][i] += dp[n-1][i-A[n-1]]
if dp[-1][-1]:
    YES()
NO()