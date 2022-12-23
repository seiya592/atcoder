"""
2022/12/10 17:51:34
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
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(500000)
INF = 10**17


N,A = IIS()
P = LIIS()
Q = LIIS()
R = LIIS()
PQR = [(p,q,r) for p,q,r in zip(P,Q,R)]
dp = [[INF]*3 for _ in range(N+1)]
dp[1][0] = P[0]
dp[1][1] = Q[0]
dp[1][2] = R[0]

for n in range(2,N+1):
    for i in range(3):
        for j in range(3):
            dp[n][i] = min(dp[n][i], dp[n-1][j] + PQR[n-1][i] - (0 if i != j else A))
print(min(dp[-1]))