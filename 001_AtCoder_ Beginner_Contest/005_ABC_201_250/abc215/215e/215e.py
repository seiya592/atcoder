def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10

d = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
     }
ALL = 2 ** 10
MOD = 998244353
N = II()
S = I()
T = []
for s in S:
    T.append(d[s])

# dp[n番目のコンテストまでで][i(bit)のコンテストに参加し][最後に参加したコンテスト] = 組み合わせ数
dp = [[[0] * (10+1) for _ in range(ALL)] for _ in range(N+1)]
dp[0][0][0] = 1

#配る
for n in range(N):
    for i in range(ALL):
        for j in range(10+1):
            #参加しない
            dp[n+1][i][j] += dp[n][i][j] % MOD
            if i & (1<<T[n]) == 0 or j == T[n]+1:   # まだコンテストに参加していない or 最後に行ったコンテストと同じ
                #参加
                dp[n+1][i|(1<<T[n])][T[n]+1] += dp[n][i][j] % MOD

ans = 0
for d in dp[N]:
    for m in d[1:]:
        ans += m % MOD
print(ans % MOD)