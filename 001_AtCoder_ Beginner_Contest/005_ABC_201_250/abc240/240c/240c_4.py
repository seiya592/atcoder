"""
2022/12/10 11:43:23
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


N,X = IIS()
AB = LLIIS(N)

dp = [[0]*(10000*2+1) for _ in range(N+1)]
dp[0][0] = 1

#配る
for n in range(N):
    for i in range(X):
        dp[n+1][i+AB[n][0]] += dp[n][i]
        dp[n + 1][i + AB[n][1]] += dp[n][i]
if dp[N][X]:
    YES()
NO()