def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)

N = II()
T = []
for _ in range(N):
    T.append(II())

ALL = 2 ** N
ans = 10**10
Tsum = sum(T)
for n in range(ALL):
    tmp = 0
    for i in range(N):
        if has_bit(n,i):
            tmp += T[i]
    ans = min(max(tmp,Tsum-tmp),ans)
print(ans)