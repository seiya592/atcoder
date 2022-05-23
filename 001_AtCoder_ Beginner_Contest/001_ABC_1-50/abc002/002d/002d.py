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

N,M = IIS()
E = [[i] for i in range(N+1)]
for _ in range(M):
    x,y = IIS()
    E[x].append(y)
    E[y].append(x)

ALL = 2 ** N
ans = 0
for n in range(ALL):
    tmp = []
    for i in range(N):
        if has_bit(n,i):
            tmp.append(i+1)

    flg = True
    for t in tmp:
        for i in tmp:
            if not i in E[t]:
                flg = False
                break

    if flg:
        ans = max(ans,len(tmp))
print(ans)