def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,A,B = IIS()
X = LIIS()
dp = [[0]*A for _ in range(N+1)]
dp[0][0] = 1
for n in range(N):
    for i in range(A):
        dp[n+1][i] += dp[n][i]
        dp[n+1][(i+X[n])%A] += dp[n][i]
print('Yes' if dp[N][B] else 'No')