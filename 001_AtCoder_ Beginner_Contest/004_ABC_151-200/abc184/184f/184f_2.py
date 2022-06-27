import bisect


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0

N, K = IIS()
T = LIIS()

A = []
B = []
for i in range(N):
    if i%2:
        A.append(T[i])
    else:
        B.append(T[i])


def calc(lst):
    l = len(lst)
    ALL = 2 ** l
    ans = []

    for n in range(ALL):
        tmp = 0
        for i in range(l):
            if has_bit(n,i):
                tmp += lst[i]
        ans.append(tmp)
    ans.sort()
    return ans


As = calc(A)
Bs = calc(B)
ans = 0
for a in As:
    if a > K:
        break
    ans = max(ans,a +  Bs[bisect.bisect_right(Bs, K - a)-1])
print(ans)
