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


N = II()
A = LIIS()

# bit全探索
ALL = 2 ** N
ans = 10 ** 100
for n in range(ALL):
    xor_lst = []

    old = has_bit(n,0)
    or_sum = 0
    for i in range(N):
        if has_bit(n, i):
            now = True
        else:
            now = False

        if now == old:
            or_sum |= A[i]
        else:
            old = now
            xor_lst.append(or_sum)
            or_sum = A[i]
    else:
        xor_lst.append(or_sum)

    tmp = 0
    for o in xor_lst:
        tmp ^= o

    ans = min(ans, tmp)

print(ans)