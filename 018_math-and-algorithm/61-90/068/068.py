"""
2022/08/09 22:02:12
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
from functools import reduce
import math
def my_lcm(numbers):
    """
    O(N log (max(*numbers)))
    リスト内のすべての要素の最大公約数を求める
    :param numbers:
    :return:numbersの要素の中の最大公約数
    """

    def my_lcm_base(x, y):
        return (x * y) // math.gcd(x, y)
    return reduce(my_lcm_base, numbers, 1)
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0

N, K = IIS()
V = LIIS()

ALL = 2 ** K

ans = 0

for n in range(ALL):
    t = []
    for i in range(K):
        if has_bit(n,i):
            t.append(V[i])
    if len(t):
        c = my_lcm(t)
        if len(t) % 2:
            ans += N // c
        else:
            ans -= N // c
print(ans)