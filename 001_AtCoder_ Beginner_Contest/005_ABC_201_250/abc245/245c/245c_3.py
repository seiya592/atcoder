"""
2022/12/10 11:19:07
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


N, K = IIS()
AB = LLIIS(2)

dp = [[-INF]*2 for _ in range(N+1)]
dp[0][0] = AB[0][0]
dp[0][1] = AB[1][0]
for n in range(1,N):
    for i in range(2):
        for j in range(2):
            if abs(dp[n-1][i] - AB[j][n]) <= K:
                dp[n][j] = AB[j][n]
if dp[N-1][0] != -INF or dp[N-1][1] != -INF:
    YES()
NO()