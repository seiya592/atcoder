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


N = II()
A = LIIS()
MOD = 998244353
ans = 0
#合計1個~N個選ぶ
for i in range(1,N+1):
    dp = [[[0]*i for _ in range(i+1)] for _ in range(N+1)]
    # dp[先頭からj個まで選べる][選んだ個数k][余りの数l]
    dp[0][0][0] = 1
    for j in range(N):
        for k in range(i+1):
            for l in range(i):
                # 選ばない
                dp[j+1][k][l] += dp[j][k][l] % MOD
                # 選ぶ
                if i > k:
                    dp[j+1][k+1][(l+A[j]) % i] += dp[j][k][l] % MOD
    ans += dp[-1][-1][0] % MOD
    ans %= MOD
print(ans)