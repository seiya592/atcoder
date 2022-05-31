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

# 解説AC

N = I()

dp = [[[0]*2 for _ in range(len(N)+1)] for _ in range(len(N)+1)]
# dp[n桁目][1がk個][未満フラグ]
dp[0][0][0] = 1
for n in range(len(N)):
    r = int(N[n])
    for k in range(len(N)):
        for i,t in enumerate([r,9]):
            for j in range(t+1):
                dp[n+1][k+(j==1)][i|(r>j)] += dp[n][k][i]

ans = 0
for i in range(len(N)+1):
    ans += i * sum(dp[len(N)][i])
print(ans)