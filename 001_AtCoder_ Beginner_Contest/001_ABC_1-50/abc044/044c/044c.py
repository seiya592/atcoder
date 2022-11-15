"""
2022/09/18 10:03:24
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


N,A = IIS()
X = LIIS()

dp = [[[0]*(N+1) for _ in range(50*A+1)] for _ in range(N+1)]
#dp[n枚まで見て][値aを][k枚で作った時の] = 組み合わせ数
dp[0][0][0] = 1

for n in range(N):
    for a in range(50*A+1):
        for k in range(N+1):
            dp[n+1][a][k] += dp[n][a][k]
            if k < N and a+X[n] < 50*A+1:
                dp[n+1][a+X[n]][k+1] += dp[n][a][k]
ans = 0
for n in range(1,N+1): #選んだ枚数
    ans +=dp[-1][A*n][n]
print(ans)