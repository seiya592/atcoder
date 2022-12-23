"""
2022/12/10 18:06:33
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



N,A,B = IIS()
PQR = LLIIS(3)

dp = [[[INF] * 3 for _ in range(3)] for _ in range(N+1)]
#dp[日数][最終店舗][連続数]
dp[1][0][0] = PQR[0][0]
dp[1][1][0] = PQR[1][0]
dp[1][2][0] = PQR[2][0]

for n in range(2,N+1):
    for i in range(3):      # 前回店舗
        for j in range(3):
            for k in range(3): #今回店舗
                for l in range(3):
                    if i!=k and j != 0:
                        continue
                    if i == k and not (j -1 == l or (j == 2 and l == 2)):
                        continue
                    dp[n][k][j] = min(dp[n][k][j], dp[n-1][i][l] + PQR[k][n-1] - (0 if i != k or j == 0 else A if j == 1 else B))

ans = INF
for i in range(3):
    for j in range(3):
        ans = min(ans, dp[-1][i][j])
print(ans)