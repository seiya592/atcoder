def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20


# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_c

N,M = IIS()
dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
for _ in range(N):
    a,b,c,d = IIS()
    dp[a][b][c] = max(dp[a][b][c],d)

# dp[aがi以上][bがj以上][cがk以上]＝ の人の最高年収
for i in range(101):
    for j in range(101):
        for k in range(101):
            # dp[i][j][k] = max(dp[i][j][k],dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
            dp[i][j][k] = max(dp[max(i - 1, 0)][j][k], dp[i][max(j - 1, 0)][k], dp[i][j][max(k - 1, 0)], dp[i][j][k])

for _ in range(M):
    a,b,c = IIS()
    print(dp[a][b][c])