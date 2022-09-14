"""
2022/08/08 23:23:18
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

X, Y = IIS()

#連立方程式
"""
(i+1,j+2)を行う回数を A
(i+2,j+1)を行う回数を B

A+2B = X
2A+B = Y

#連立方程式を解く
A = X-2B
B = Y-2A

A = X-2(Y-2A)
  = (2Y - X) / 3
B = (2X - Y) / 3

整数で割れない場合は解無し
割った数が負数の場合も解無し
"""

if (2 * Y - X) % 3 or (2 * X - Y) % 3:
    print(0)    #解無し
    exit()

A = (2 * Y - X) // 3
B = (2 * X - Y) // 3

if A < 0 or B < 0:
    print(0)
    exit()

"""
(A+B)の行動を行う中で B回 (i+2,j+1) を選択する
(A+B) Comb B
→ (A+B)! // B! * (A+B-B)!
"""
MOD = 10**9+7

def calc(n, mod):
    """
    nの階乗を求める
    """
    s = 1
    for i in range(2, n+1):
        s *= i
        s %= mod
    return s

a = calc(A+B, MOD)
b = calc(B,MOD) * calc(A, MOD)

print(Division(a,b,MOD))
