import math


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

D,G = IIS()
PC = LLIIS(D)

ALL = 2 ** D

#bitが立っている部分は全部解く
#全部解いた後にbitが立っていない所で一番点数が高いところを解く
ans = 10**10
for n in range(ALL):
    score = 0
    cnt = 0
    for i in range(D):
        if has_bit(n,i):
            score += ((i+1)*100)*PC[i][0] + PC[i][1]
            cnt += PC[i][0]
    if G - score > 0:
        for i in reversed(range(D)):
            if not has_bit(n,i):
                t = math.ceil((G - score) / ((i+1)*100))
                cnt += min(t,PC[i][0])
                score += min(t,PC[i][0]) * ((i+1) * 100)
                break
    if G - score <= 0:
        ans = min(ans,cnt)
print(ans)
