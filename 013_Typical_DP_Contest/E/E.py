def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


D = II()
N = II()
Nstr = str(N)
dp = [[[0] * 2 for _ in range(D)] for _ in range(len(Nstr) + 1)]
# dp[i桁目][現時点でのDで割ったあまり][N未満か]
dp[0][0][0] = 1
for i in range(len(Nstr)):
    for j in range(D):
        for k in range(2):
            loop = 9 if k else int(Nstr[i])
            for d in range(loop+1):
                dp[i+1][(j+d) % D][k | (d < int(Nstr[i]))] += dp[i][j][k]
                dp[i + 1][(j  + d) % D][k | (d < int(Nstr[i]))] %= 1000000007

print(dp[len(Nstr)][0][0] + dp[len(Nstr)][0][1] -1) # 0は含めないので-1