def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

N = II()

dp = [[0]*10 for _ in range(N+1)]
# dp[n桁まで][最後の数字(0は使わない)]

for i in range(1,10):
    dp[1][i] = 1


for n in range(2, N+1):
    for i in range(1, 10):
        s = max(1, i-1)
        e = min(9, i+1)
        for j in range(s,e+1):
            dp[n][i] += dp[n-1][j] % 998244353

print(sum(dp[N]) % 998244353)

