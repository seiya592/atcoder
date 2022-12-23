"""
2022/12/10 18:42:35
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
# # import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(500000)
INF = 10**17


N,M = IIS()
W = LIIS()

dp = [[[0] * 2 for _ in range(M+1)] for _ in range(N+1)]

#dp[n個目までを見た][重さ][偶奇] = 組み合わせ
dp[0][0][0] = 1
for n in range(1,N+1):
    for i in range(M+1):
        for k in range(2):
            # 選ばない
            dp[n][i][k] += dp[n-1][i][k]
            #選ぶ
            if i - W[n-1] < 0:
                continue
            dp[n][i][k] += dp[n-1][i-W[n-1]][1^k]
if dp[N][M][1]:
    YES()
NO()