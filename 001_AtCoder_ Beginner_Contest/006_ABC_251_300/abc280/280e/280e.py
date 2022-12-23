"""
2022/12/03 20:42:28
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

N,P = IIS()
MOD = 998244353

dp = [0] * (N+3)

for i in range(N-1,-1,-1):
    dp[i] += Division((dp[i+1]+1) * (100-P), 100, MOD)
    dp[i] += Division((dp[i+2]+1) * (P), 100, MOD)
print(dp[0]%MOD)

# dp = [0] * (N+3)
# o_dp = [0] * (N+3)
# o_dp[0] = 1
# ans = 1
# for i in range(0,N):
#     dp = [0] * (N + 3)
#     for d in range(i,min(i*2+1,N)):
#         #配る
#         # dp[d+2] = o_dp[d] * P
#         # dp[d+1] = o_dp[d] * (100-P)
#         dp[min(d+2,N)] = Division(o_dp[d] * P, 100, MOD)
#         dp[min(d + 1,N)] += Division(o_dp[d] * (100-P), 100, MOD)
#     if dp[N]:
#         ans += dp[N]
#         ans %= MOD
#     o_dp = dp
# print(o_dp[N]%MOD)
# pass