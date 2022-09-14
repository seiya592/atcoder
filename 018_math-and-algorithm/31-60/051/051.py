"""
2022/08/08 22:27:22
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
import sys
sys.setrecursionlimit(500000)
INF = 10**10

import math
def mod_pow(a,b,m):
    """
    a ** b mod m を求める
    pow(a,b,m)より早い
    """
    ALL = math.ceil(math.log2(b)) + 1
    MOD = 10 ** 9 + 7

    ans = 1
    t = a
    for i in range(ALL):
        if b & (1 << i):
            ans *= t
            ans %= MOD
        t *= t
        t %= MOD
    return ans

def Division(a,b,m):
    """
    a / b mod m を求める
    :param a: 分子
    :param b: 分母
    :param mod: 余り
    :return:
    """
    return a * mod_pow(b, m-2, m) % m

X, Y = IIS()
MOD = 10**9+7

# (X+Y) C (X)を求める
def calc(n, mod):
    """
    nの階乗を求める
    """
    s = 1
    for i in range(2, n+1):
        s *= i
        s %= mod
    return s

a = calc(X+Y, MOD)
b = calc(X, MOD) * calc((X+Y)-X, MOD)

print(Division(a,b,MOD))

