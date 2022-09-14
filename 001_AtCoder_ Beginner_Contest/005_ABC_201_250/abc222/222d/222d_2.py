"""
2022/09/01 18:07:34
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
INF = 10**10


N = II()
A = LIIS()
B = LIIS()

dp = [[0] * 3001 for _ in range(N+1)]
dp[0][0] = 1
for n in range(1,N+1):
    s = 0
    for i in range(B[n-1]+1):
        s += dp[n-1][i] % 998244353

        if A[n-1] <= i:
            dp[n][i] = s
print(sum(dp[-1]) % 998244353)