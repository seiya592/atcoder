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
INF = 10**10


A,B,C = IIS()

dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
#dp[金][銀][銅][0→金 1→銀 2→銅が選ばれる] = 期待値

dp[A][B][C] = 1

for i in range(A,100):
    for j in range(B, 100):
        for k in range(C, 100):
            dp[i+1][j][k] += dp[i][j][k] * i / (i+j+k)
            dp[i][j+1][k] += dp[i][j][k] * j / (i + j + k)
            dp[i][j][k+1] += dp[i][j][k] * k / (i + j + k)
            # for n in range(3):
            #     t = [i,j,k]
            #     dp[i][j][k][n] = t[n] / (i+j+k) * dp[i][j][k][n]

ans = 0
for i in range(A,100):
    for j in range(B, 100):
        for k in range(C, 100):
            ans += dp[i][j][k]
print(ans)