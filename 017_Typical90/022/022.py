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


def my_gcd(numbers):
    """
        O(?)
        リスト内のすべての要素の最小公倍数を求める
        :param numbers:
        :return:numbersの要素の中の最小公倍数
        """
    from functools import reduce
    import math
    return reduce(math.gcd, numbers)

ABC = LIIS()

gcd = my_gcd(ABC)

ans = 0
for a in ABC:
    ans += a // gcd -1
print(ans)