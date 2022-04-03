def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


# def has_bit(n,i):
#     """
#     nで表現される集合に要素iが含まれているかを判定
#     :param n:int 集合
#     :param i:int 要素
#     :return:bool True→含まれている False→含まれていない
#     """
#     return (n & (1<<i) > 0)

N = II()
S = I()
flg = True
while flg:

    ck = 0
    for s in S:
        if s == '(':
            ck += 1
        else:
            ck += -1

        if ck < 0:
            S = '(' + S
            break

    else:
        if ck == 0:
            flg = False
        else:
            S += ')'

print(S)