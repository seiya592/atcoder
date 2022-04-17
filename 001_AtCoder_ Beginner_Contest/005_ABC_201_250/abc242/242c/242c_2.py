def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()

dp = [[0] * 11 for _ in range(N)]
# dp[i+1桁目の組み合わせ数][一番大きい位の値1~9(0,10は要素外アクセス対策でとりあえず用意する)]
for i in range(1,10):
    dp[0][i] = 1
#配るDP
for i in range(N-1):
    for n in range(1,10):
        for t in [-1,0,1]:  #差が1以内の値に配る
            dp[i+1][n+t] += dp[i][n]
            dp[i + 1][n + t] %= 998244353

print(sum(dp[N-1][1:10])%998244353)