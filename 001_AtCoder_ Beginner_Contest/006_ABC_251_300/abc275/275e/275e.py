"""
2022/10/29 20:52:09
"""
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17
MOD= 998244353
import math
def mod_pow(a,b,m):
    """
    Division で使用する関数
    a ** b mod m を求める
    組み込み関数 pow(a,b,m)より早い
    """
    ALL = math.ceil(math.log2(b)) + 1

    ans = 1
    t = a
    for i in range(ALL):
        if b & (1 << i):
            ans *= t
            ans %= m
        t *= t
        t %= m
    return ans
def Division(a,b,m):
    """
    a / b mod m を求める (モジュラー逆数で求める)
    :param a: 分子
    :param b: 分母
    :param m: 余り　素数であること
    :return: a / b mod m
    """
    return a * mod_pow(b, m-2, m) % m

N,M,K = IIS()
dp = [[0] * (N+1) for _ in range(K+1)]
dp[0][0] = 1
for i in range(K):      # 何回回したか
    for j in range(N): #マス目
        if i and j == 0:
            continue
        if dp[i][j] == 0:
            continue
        for k in range(1,M+1):
            if j + k <= N:
                dp[i+1][j+k] += dp[i][j]
                dp[i + 1][j + k] %= MOD
            else:
                dp[i+1][N-(k-(N-j))] += dp[i][j]
                dp[i + 1][N - (k - (N - j))] %= MOD
            dp[i+1][0] += dp[i][j]
            dp[i+1][0] %= MOD

ans = 0
for n in range(1,K+1):
    ans += Division(dp[n][-1],mod_pow(M,n,MOD),MOD)
    ans %= MOD
print(ans)
