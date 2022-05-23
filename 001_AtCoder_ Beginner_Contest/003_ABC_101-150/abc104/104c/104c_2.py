def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


#dpで解いてみる

D,G = IIS()
G //= 100
P = []
C = []
ALL = 0
INF = -10**10
for i in range(D):
    p,c = IIS()
    P.append(p)
    C.append(c//100)
    ALL += p

dp = [[INF]*((ALL+1)*2) for _ in range(D+1)]
# dp[n番目までの問題][i問解いたときに]=一番大きいスコア
dp[0][0] = 0
#くばる
for n in range(D):
    for i in range(ALL):
        for j in range(P[n]):
            dp[n+1][i+j] = max(dp[n+1][i+j], dp[n][i]+((n+1)*(j)))
        else:
            dp[n+1][i+P[n]] = max(dp[n+1][i+P[n]], dp[n][i]+((n+1)*(P[n]))+C[n])

for i,n in enumerate(dp[D]):
    if n >= G:
        print(i)
        exit()