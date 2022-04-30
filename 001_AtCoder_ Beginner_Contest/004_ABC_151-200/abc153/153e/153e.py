def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


H,N = IIS()
AB = LLIIS(N)

#個数制限なしナップサック
dp = [[10**10] * (H+1) for _ in range(N+1)]
#dp[n番目の商品で][削った体力量] = 最小コスト
dp[0][0] = 0
for n in range(N):
    for d in range(H+1):
        dp[n+1][d] = min(dp[n][d],dp[n+1][d]) # 選択しない場合
        if d+AB[n][0] <= H:
            dp[n+1][d+AB[n][0]] = min(dp[n+1][d+AB[n][0]],dp[n+1][d]+AB[n][1])
        else:
            dp[n + 1][H] = min(dp[n + 1][H], dp[n + 1][d] + AB[n][1])
print(dp[N][H])