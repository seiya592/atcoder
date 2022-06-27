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

N, K, P = IIS()
A = []
B = []
T = LIIS()

for i, t in enumerate(T):
    if i % 2 == 0:
        A.append(t)
    else:
        B.append(t)


def calc(lst):
    num = len(lst)
    ALL = 2 ** num
    ans = [[] for _ in range(num+1)]

    for n in range(ALL):
        cnt = 0
        tmp = 0
        for i in range(num):
            if has_bit(n,i):
                cnt += 1
                tmp += lst[i]
        ans[cnt].append(tmp)
    return ans


As = calc(A)
Bs = calc(B)

for i in range(len(Bs)):
    Bs[i].sort()
ans = 0
for i in range(K+1):
    if i >= len(As) or K - i >= len(Bs):
        continue
    for a in As[i]:
        ans += bisect.bisect_right(Bs[K-i], P - a)
print(ans)
