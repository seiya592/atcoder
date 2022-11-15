"""
2022/10/17 20:00:09
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


N, W = IIS()
WV = LLIIS(N)

dp = [[-INF] * (W+1) for _ in range(N+1)]
dp[0][0] = 0

# 配る
for n in range(N):
    w,v = WV[n]
    for i in range(W+1):
        dp[n+1][i] = max(dp[n+1][i], dp[n][i])

        if i + w <= W:
            dp[n+1][i+w] = max(dp[n+1][i+w], dp[n][i] + v)

print(max(dp[-1]))