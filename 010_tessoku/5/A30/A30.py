"""
2022/11/14 19:48:45
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


"""
E8本　p.187
"""

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

N,R = IIS()

MOD = 10**9+7

a = 1
for i in range(1,N+1):
    a *= i
    a %= MOD

b = 1
for i in range(1,R+1):
    b *= i
    b %= MOD
for i in range(1,N-R+1):
    b *= i
    b %= MOD

print(Division(a,b,MOD))