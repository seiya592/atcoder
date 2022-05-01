def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


S = I()
T = I()

Sl = len(S)
Tl = len(T)

dp = [[0] * (Tl+1) for _ in range(Sl+1)]
#dp[Sのi文字目][Tのi文字目]=までの最長部分文字列
# もらう
for i in range(1,Sl+1):
    for j in range(1,Tl+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)
        dp[i][j] = max(dp[i-1][j],dp[i][j])
        dp[i][j] = max(dp[i][j-1],dp[i][j])
print(dp[Sl][Tl])