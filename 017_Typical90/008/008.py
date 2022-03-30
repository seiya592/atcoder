def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

MOD = 10**9 + 7
N = II()
S = I()
AT = 'atcoder'

dp = [[0] * len(AT) for _ in range(N+1)]
# dp[i番目の文字まで][特定の文字列] = 組み合わせ

for i in range(1,N+1):
    for j, a in enumerate(AT):
        if S[i-1] == a:
            if j == 0:
                dp[i][j] = (1 + dp[i - 1][j]) % MOD
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][len(AT)-1])