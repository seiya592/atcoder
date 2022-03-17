def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(float, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
P = LIIS()

dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1,N+1):  # 現在のコイン
    for j in range(i+1):    # 表の枚数
        if j == 0:
            dp[i][j] = dp[i-1][j] * (1-P[i-1])      # 全部裏は1つ前を掛ける
        else:
            dp[i][j] = (dp[i-1][j-1] * P[i-1]) + (dp[i-1][j] * (1 - P[i-1]))        # 全部表の場合は後ろの式が0になる それ以外はコイン1つ前の状態から今のコインが表か裏かで表の数を同じにして足す

print(sum(dp[N][N//2+1:]))