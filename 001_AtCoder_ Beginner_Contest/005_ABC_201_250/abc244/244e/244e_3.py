def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M,K,S,T,X = IIS()
E = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

# dp[スタートからk番目][最後の頂点][0:Xを偶数回踏んでいる 1:奇数回踏んでいる]
dp = [[[0]*2 for _ in range(N+1)] for _ in range(K+1)]

#配る
dp[0][S][0] = 1
for k in range(K):
    for n in range(N+1):
        for o in range(2):
            for e in E[n]:
                if e != X:
                    dp[k+1][e][o] += dp[k][n][o]
                    dp[k + 1][e][o] %= 998244353
                else:
                    dp[k+1][e][o^1] += dp[k][n][o]
                    dp[k + 1][e][o^1] %= 998244353
print(dp[K][T][0])
