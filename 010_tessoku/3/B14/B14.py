"""
2022/10/13 19:34:45
"""
import bisect


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
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0


N, K = IIS()
A = LIIS()
B = [a for i,a in enumerate(A) if i%2==0]
C = [a for i,a in enumerate(A) if i%2==1]

def calc(L):
    ALL = 2 ** len(L)
    ans = []
    for n in range(ALL):
        total = 0
        for i in range(len(L)):
            if has_bit(n,i):
                total += L[i]
        ans.append(total)
    return ans


X = calc(B)
Y = calc(C)
Y.sort()
for x in X:
    t = bisect.bisect_left(Y,K-x)
    if t < len(Y) and Y[t] == K-x:
        YES()
NO()