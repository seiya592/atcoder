"""
2022/10/19 19:49:38
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

"""
初期化していない場合のhackケース
7
7 3 4 5 6 7
7 4 5 6 6 7
"""

N = II()
A = [0] + LIIS()
B = [0] + LIIS()

dp = [-INF] * (N+1)
dp[1] = 0
for i in range(1,N):
    dp[A[i]] = max(dp[i] + 100, dp[A[i]])
    dp[B[i]] = max(dp[i] + 150, dp[B[i]])

print(dp[-1])