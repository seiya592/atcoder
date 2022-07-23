import itertools


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [list(map(int,list(I()))) for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
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
def fnc_cnt(x):
    tmp = []
    x += ALL
    for i in range(H):
        tmp.append(has_bit(x,i))
    return len(list(itertools.groupby(tmp)))

H,W,K = IIS()
S = LI(H)

ALL = 2 ** H
ans = INF
for n in range(ALL):
    cnt = fnc_cnt(n)
    d = [0] * cnt
    tmp = 0
    flg = True
    for j in range(W):
        now = 0
        nowbit = n & 1
        for i in range(H):
            if has_bit(n,i) != nowbit:
                now += 1
                nowbit ^= 1
            d[now] += S[i][j]

        if any([(dd > K) for dd in d]):
            if flg and cnt != H:
                cnt = INF
                break #横１マスでも規定以上になる
            tmp += 1
            flg = True
            d = [0] * cnt

            now = 0
            nowbit = n & 1
            for i in range(H):
                if has_bit(n, i) != nowbit:
                    now += 1
                    nowbit ^= 1
                d[now] += S[i][j]
        else:
            flg = False

    ans = min(ans, cnt - 1 + tmp)
print(ans)