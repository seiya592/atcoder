def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20
from functools import reduce
import math
def my_lcm(numbers):
    """
    O(N log (max(*numbers)))
    リスト内のすべての要素の最小公倍数を求める
    :param numbers:
    :return:numbersの要素の中の最小公倍数
    """

    def my_lcm_base(x, y):
        return (x * y) // math.gcd(x, y)
    return reduce(my_lcm_base, numbers, 1)


N,A,B = IIS()

def Arithmetic_progression(a,d,n):
    """
    等差数列の和を求める

    l = [1,5,9,13,17]
    a = 1 l[0]
    d = 4 l[n+1] - l[n]
    n = 5 len(l)
    return = 45

    :param a:初項
    :param d:公差
    :param n:項数
    :return:等差数列の和
    """
    return n * (a+(n*d)) // 2

Ns = Arithmetic_progression(1,1,N)
As = Arithmetic_progression(A,A,N//A)
Bs = Arithmetic_progression(B,B,N//B)
AB = my_lcm([A,B])
ABs = Arithmetic_progression(AB,AB,N//AB)
print(Ns-As-Bs+ABs)


# # TLE  これでACな言語もあるらしいがpythonだとダメ
# Ns = sum(range(N+1))
# As = sum(range(0,N+1,A))
# Bs = sum(range(0,N+1,B))
# ABs = sum(range(0,N+1,my_lcm([A,B])))
# print(Ns-As-Bs+ABs)