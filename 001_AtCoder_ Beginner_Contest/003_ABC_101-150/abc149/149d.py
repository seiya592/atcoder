def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,K = IIS()
R,S,P = IIS()
T = I()
d = {'r':P,'s':R,'p':S}
dp = [[0,False] for _ in range(N+1)]
#dp[n番目の手,勝ち→True負け→False] = 最大値
for n in range(N):
    if n < K:
        #K番目までは常に勝ち続けていい
        dp[n+1][0] = dp[n][0] + d[T[n]]
        dp[n+1][1] = True
    else:
        #K番前で勝っている and K番前と手が同じ場合は今回は勝てない （手が違う場合だったり負けている場合は勝ってよい）
        if T[n] == T[n-K] and dp[n-K+1][1]:
            dp[n+1][0] = dp[n][0]
            dp[n+1][1] = False
        else:
            dp[n + 1][0] = dp[n][0] + d[T[n]]
            dp[n + 1][1] = True
print(dp[N][0])