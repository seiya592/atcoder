import math


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20
def has_bit(n,i):
    """
    nで表現される集合に要素iが含まれているかを判定
    :param n:int 集合
    :param i:int 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1<<i) > 0)

N, K = IIS()
LEN = math.floor(math.log2(K)) + 1
D = [[-1]*LEN for _ in range(10**5+1)]

#設定
for i in range(10**5+1):
    tmp = i
    calc = 0
    while tmp:
        calc += tmp % 10
        tmp //= 10
    D[i][0] = (calc + i) % 10**5
for j in range(1,LEN):
    for i in range(10**5+1):
        D[i][j] = D[D[i][j-1]][j-1]


now = N
for i in range(LEN):
    if has_bit(K,i):
        now = D[now][i]
print(now)