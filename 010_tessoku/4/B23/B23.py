"""
2022/10/21 19:29:47
"""
import math


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0

def calc(x,y,a,b):
    return math.sqrt((x-a)**2 + (y-b)**2)

N = II()
XY = LLIIS(N)

ALL = 2 ** N

def calc2(s):
    dp = [[INF] * N for _ in range(ALL)]
    dp[0][s] = 0

    for n in range(ALL):
        for i in range(N):  #現在地
            for j in range(N):  #行先
                if not has_bit(n,j) and i != j:    # 現在地に行ったことがあって行先に行ったことがない場合（矛盾がない場合）
                    x,y = XY[i]
                    a,b = XY[j]
                    dp[n|(1<<j)][j] = min(dp[n|(1<<j)][j], dp[n][i] + calc(x,y,a,b))

    return dp[ALL-1][s]


print(calc2(0))