def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
STATUS = [LIIS() for _ in range(N)]

# 二分探索で一定の能力の編成が行えるかをチェック

ok = 0
ng = 10 ** 9 + 1


def check(n):
    # 各メンバーがn以上の能力を持っていたらBitFigを立てる
    set_list = set()
    for a in STATUS:
        tmp = 0
        for i in range(5):
            if a[i] >= n:
                tmp |= 1 << i
        set_list.add(tmp)

    # N^3 (N=32)なので間に合うはず
    for i in set_list:
        for j in set_list:
            for k in set_list:
                if i | j | k == 31:
                    return True
    return False

while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)