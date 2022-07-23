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
    return n * (2*a+((n-1)*d)) // 2

A,B,C = IIS()
MOD = 998244353
A = Arithmetic_progression(1,1,A) % MOD
B = Arithmetic_progression(1,1,B) % MOD
C = Arithmetic_progression(1,1,C) % MOD

print((A*B*C)%MOD)
