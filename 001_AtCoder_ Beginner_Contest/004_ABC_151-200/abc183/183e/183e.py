def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


H,W = IIS()
S = LLIIS(H)

dp = [[[0] * 4 for _ in range(W+1)] for _ in range(H+1)]
#dp[row][col][0:現在位置の組み合わせ数 1:縦の累積和 2:横の累積和 3:斜めの累積和]

#貰うDP
dp[0][0][0] = 0 # 初期設定はする必要なさそう、for文内の例外処理で行う 0,0は架空のマス
dp[0][0][1] = 0
dp[0][0][2] = 0
dp[0][0][3] = 0

for r in range(1,H+1):
    for c in range(1,W+1):
        if r == 1 and c == 1:
            dp[1][1][0] = 1
            # 累積和更新
            dp[r][c][1] += dp[r][c][0] + dp[r - 1][c][1]
            dp[r][c][2] += dp[r][c][0] + dp[r][c - 1][2]
            dp[r][c][3] += dp[r][c][0] + dp[r - 1][c - 1][3]

        elif S[r-1][c-1] == '.':
            dp[r][c][0] = dp[r-1][c][1] + dp[r][c-1][2] + dp[r-1][c-1][3]

            #累積和更新
            dp[r][c][1] += dp[r][c][0] + dp[r-1][c][1]
            dp[r][c][2] += dp[r][c][0] + dp[r][c-1][2]
            dp[r][c][3] += dp[r][c][0] + dp[r-1][c-1][3]

        for i in range(4):
            dp[r][c][i] %= 10**9+7
print(dp[H][W][0])
