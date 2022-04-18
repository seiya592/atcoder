def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
A = LIIS()
dp = [[0]*10 for _ in range(N)]
#dp[i番目のA][一番左の数字] = 組み合わせ数
dp[0][A[0]] = 1
for n in range(1,N):
    for m in range(10):
        dp[n][(A[n]+m)%10] += dp[n-1][m]%998244353
        dp[n][(A[n]*m)%10] += dp[n-1][m]%998244353
for d in dp[N-1]:
    print(d%998244353)
