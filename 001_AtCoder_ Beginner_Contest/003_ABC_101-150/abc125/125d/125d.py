def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
#解説AC

N = II()
A = LIIS()

dp = [[0] * 2 for _ in range(N)]
# dp[i+1番目番目の数字まで][0→反転無し1→反転有]
dp[0][0] = A[0]
dp[0][1] = -A[0]
#貰うdp
for n in range(1,N):
    for r in range(2):
        dp[n][r] = max(dp[n-1][r]+A[n], dp[n-1][r^1]-A[n])
print(dp[N-1][0])
