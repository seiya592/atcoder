"""
2022/10/14 18:59:05
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


N = II()
A = LIIS()
B = LIIS()

dp = [INF] * N
dp[0] = 0
dp[1] = A[0]
for n in range(2,N):
    dp[n] = min(dp[n-1] + A[n-1], dp[n-2] + B[n-2])
print(dp[-1])