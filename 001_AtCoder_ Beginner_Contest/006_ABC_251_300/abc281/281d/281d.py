"""
2022/12/10 20:46:09
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
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')        
sys.setrecursionlimit(500000)
INF = 10**17


N,K,D = IIS()
A = LIIS()

dp = [[[-INF] * (D) for _ in range(K+1) ]for _ in range(N+1)]
#dp[nまで見た][k個まで含まれている][値%Dの余り] = 最大値
dp[0][0][0] = 0
for n in range(N):
    for k in range(K+1):
        for d in range(D):
            if dp[n][k][d] == -INF:
                continue
            #選ばない
            dp[n+1][k][d] = max(dp[n+1][k][d], dp[n][k][d])

            #選ぶ
            if k + 1 <= K:
                dp[n+1][k+1][(d+A[n])%D] = max(dp[n+1][k+1][(d+A[n])%D], dp[n][k][d] + A[n])

if dp[N][K][0] == -INF:
    print(-1)
else:
    print(dp[N][K][0])