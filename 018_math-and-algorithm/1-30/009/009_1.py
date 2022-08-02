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
    :return:bool True→存在する False→存在しない
    """
    return (n & (1<<i) > 0)


# 全探索

N, S = IIS()
A = LIIS()

ALL = 2 ** N

for n in range(ALL):
    tmp = 0
    for i in range(N):
        if has_bit(n, i):
            tmp += A[i]

    if S == tmp:
        print('Yes')
        exit()
print('No')