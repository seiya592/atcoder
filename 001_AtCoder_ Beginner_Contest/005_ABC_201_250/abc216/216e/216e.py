"""
2022/11/14 18:05:47
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


N,K = IIS()
A = LIIS() + [0]

A.sort(reverse=True)

now = 0
ans = 0
while now < N:
    if K - (A[now] - A[now+1]) * (now+1) >= 0:
        n = A[now] - A[now+1]
        d = -(now+1)
        a = A[now] * (now+1)

        K -= (A[now] - A[now+1]) * (now+1)
    else:
        n = (K // (now+1))
        d = -(now+1)
        a = A[now] * (now+1)

        ans += Arithmetic_progression(a, d, n)

        ans += (A[now]-n) * (K%(now+1))
        break

    ans += Arithmetic_progression(a,d,n)
    now += 1
print(ans)