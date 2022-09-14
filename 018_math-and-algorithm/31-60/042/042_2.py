"""
2022/08/07 21:06:53
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
    # return n * (a+(n*d)) // 2
    return n * (2*a+((n-1)*d)) // 2

N = II()
ans = 0

for i in range(1,N+1):
    ans += Arithmetic_progression(i, i, N//i)
print(ans)