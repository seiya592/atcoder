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

S = I()

ALL = 2 ** 3

for n in range(ALL):
    num = int(S[0])
    for i in range(3):
        if has_bit(n,i):
            num += int(S[i+1])
        else:
            num -= int(S[i+1])
    if num == 7:
        ans = S[0]
        for i in range(3):
            if has_bit(n,i):
                ans += '+'
            else:
                ans += '-'
            ans += S[i+1]
        ans += '=7'
        print(ans)
        exit()