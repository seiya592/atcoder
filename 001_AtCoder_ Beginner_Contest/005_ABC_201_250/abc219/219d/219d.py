def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)

N = II()
X,Y = IIS()
AB = LLIIS(N)
dp = [[[301] * (Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0
#dp[n番目までの弁当][Aの個数][Bの個数] = 必要n数

for n in range(N):
    for x in range(X+1):
        for y in range(Y+1):
            #選ばない場合
            dp[n+1][x][y] = min(dp[n][x][y], dp[n+1][x][y])

            if x + AB[n][0] < X and y + AB[n][1] < Y:
                dp[n+1][x+AB[n][0]][y+AB[n][1]] = min(dp[n][x][y] + 1, dp[n+1][x+AB[n][0]][y+AB[n][1]])
            elif x + AB[n][0] >= X and y + AB[n][1] >= Y:
                dp[n + 1][X][Y] = min(dp[n][x][y] + 1, dp[n + 1][X][Y])
            elif x + AB[n][0] >= X:
                dp[n + 1][X][y+AB[n][1]] = min(dp[n][x][y] + 1, dp[n + 1][X][y+AB[n][1]])
            else:
                dp[n + 1][x+AB[n][0]][Y] = min(dp[n][x][y] + 1, dp[n + 1][x+AB[n][0]][Y])
print(-1 if dp[N][X][Y] == 301 else dp[N][X][Y])