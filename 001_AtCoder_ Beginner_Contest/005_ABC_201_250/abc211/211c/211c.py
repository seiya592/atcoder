def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


S = I()
Sl = len(S)

def c(n):
    return 'chokudai'[n]

dp = [[0]*8 for _ in range(Sl+1)]
# dp[n文字目までで][chokudaiのx番目までの連結文字を作れる組み合わせ]
# 貰うDP
for n in range(1,Sl+1):
    for x in range(8):
        dp[n][x] = dp[n-1][x]
        if S[n-1] == c(x):
            dp[n][x] += dp[n-1][x-1] if x else 1    # cなら+1 それ以外なら1つ前の文字列の組み合わせを引き継ぐ
        dp[n][x] %= 10**9+7

print(dp[Sl][7])