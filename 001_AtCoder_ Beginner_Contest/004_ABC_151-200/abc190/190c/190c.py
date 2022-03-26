import itertools


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)


N, M = IIS()
AB = [LIIS() for _ in range(M)]
K = II()
CD = [LIIS() for _ in range(K)]

plate = [False] * (N+1)

# Kをbit全探索
ALL = 2 ** K
ans = 0
for n in range(ALL):
    plate = [False] * (N + 1)
    for i in range(K):
        if has_bit(n,i):
            plate[CD[i][0]] = True
        else:
            plate[CD[i][1]] = True
    tmp = 0
    for a, b in AB:
        if plate[a] and plate[b]:
            tmp += 1
    ans = max(ans, tmp)

print(ans)

for b in itertools.product(*CD):
    print(b)