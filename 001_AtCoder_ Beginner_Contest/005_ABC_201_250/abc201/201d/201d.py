"""
2022/08/25 17:38:44
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [list(I()) for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


H,W = IIS()
A = LI(H)
D = {'+':1, '-':-1, 's':0}
A[0][0] = 's'
dp = [[0]*W for _ in range(H)]

for i in reversed(range(H)):
    for j in reversed(range(W)):
        offset = 1 if (i+j)%2 else -1
        ad = D[A[i][j]] * offset
        if i == H-1 and j == W-1:
            dp[i][j] = ad
        elif i == H-1:
            dp[i][j] = dp[i][j+1] + ad
        elif j == W-1:
            dp[i][j] = dp[i+1][j] + ad
        else:
            if offset == 1:
                # takahashi Turn
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + ad
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]) + ad

if dp[0][0] >= 1:
    print('Takahashi')
elif not dp[0][0]:
    print('Draw')
else:
    print('Aoki')