"""
2022/10/17 20:06:36
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
MAX_V = 1000 * N
dp = [[INF] * (MAX_V + 1) for _ in range(N+1)]
dp[0][0] = 0

#配る
for n in range(N):
    w,v = WV[n]
    for i in range(MAX_V+1):
        dp[n+1][i] = min(dp[n][i], dp[n+1][i])
        if i+v <= MAX_V:
            dp[n+1][i+v] = min(dp[n+1][i+v], dp[n][i] + w)

ans = 0
for v in range(MAX_V+1):
    if dp[N][v] <= W:
        ans = v
print(ans)