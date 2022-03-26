def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
S = I()
X = I()

dp = [[0] * 7 for _ in range(N+1)]
# dp[i番目の桁][7で割ったあまり]
dp[N][0] = 1

for i in reversed(range(1,N+1)):    # 小さい桁からdp
    for j in range(7):      # 次の桁の数
        t1 = (j * 10) % 7   # 今回の桁が０の時の余り
        t2 = (j * 10 + int(S[i-1])) % 7 # 今回の桁がSの時の余り
        if X[i-1] == 'T':
            if dp[i][t1] or dp[i][t2]:
                dp[i-1][j] = 1      # 次の桁の余りがjの時ならば７の倍数を作れる
        else:
            if dp[i][t1] and dp[i][t2]:
                dp[i-1][j] = 1

if dp[0][0]:
    print('Takahashi')
else:
    print('Aoki')