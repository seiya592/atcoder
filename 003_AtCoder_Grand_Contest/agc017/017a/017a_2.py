def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, P = IIS()
A = LIIS()

dp = [[0] * 2 for _ in range(N+1)]
dp[0][0] = 1
# dp[n番目までの袋][1奇数0偶数] = 組み合わせ
#もらうdp

for n in range(1,N+1):
    for e in range(2):
        dp[n][e] = dp[n-1][e] + dp[n-1][(e+A[n-1])%2]       #選ばない場合+選ぶ場合
print(dp[N][P])