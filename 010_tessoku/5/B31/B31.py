"""
2022/11/14 20:03:33
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
def my_lcm_base2(x, y):
    return (x * y) // math.gcd(x, y)


from functools import reduce
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


N = II()
lst = [3,5,7]

ans = 0

for i in lst:
    ans += N // i

for i in range(3):
    for j in range(i+1,3):
        if i == j:
            continue
        ans -= N // my_lcm_base2(lst[i],lst[j])

ans += N // my_lcm(lst)

print(ans)