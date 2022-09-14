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