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
MOD = 998244353

N, M, K = IIS()

E = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

dp = [[0]*(N+1) for _ in range(K+1)]
#dp[k回目の移動で][nの街に到着する]　= 組み合わせ
dp[0][1] = 1
for k in range(K):
    s = sum(dp[k])  # 全部繋がっている場合の組み合わせ数
    s %= MOD
    for n in range(1,N+1):
        t = 0   # 足してはいけない組み合わせ数を求める
        for e in E[n]:
            t += dp[k][e]
        t += dp[k][n]   # 自身も足してはいけないので求めておく
        t %= MOD

        dp[k+1][n] = (MOD+s-t) % MOD
print(dp[K][1])
