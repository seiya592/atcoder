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


# https://atcoder.jp/contests/tdpc/tasks/tdpc_number

D = II()
N = I()

dp = [[[0]*2 for _ in range(D)] for _ in range(len(N)+1)]
dp[0][0][0] = 1
# dp[n桁目][余りがdの数の個数][0→未満フラグ]
for n in range(len(N)):
    for d in range(D):
        r = int(N[n]) #n桁目の数
        for i, t in enumerate([r+1, 10]):
            for j in range(t):
                dp[n+1][(d+j)%D][i|(r>j)] += dp[n][d][i]
                dp[n + 1][(d+j) % D][i | (r > j)] %= 10**9+7

print(sum(dp[-1][0])-1)