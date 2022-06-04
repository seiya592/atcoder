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


N,X,M = IIS()
LEN = math.floor(math.log2(N)) + 1
def func(x):
    return x**2 % M

cnt = [-1] * M
D = [-1] * M
now = X
c = 1

while True:
    if cnt[now] != -1:
        a = cnt[now] - 1    #周期に入るまでに必要なカウント
        b = c - cnt[now]  # 1周期のカウント
        c = now #周期のはじめ
        break
    cnt[now] = c
    c += 1
    next = func(now)
    D[now] = next
    now = next

if a > N:
    ans = 0
    now = X
    for _ in range(N):
        next = D[now]
        ans += now
        now = next
    print(ans)
    exit()
else:
    ans = 0
    now = X
    for _ in range(a):
        next = D[now]
        ans += now
        now = next
    N -= a
    tmp = 0
    if N // b != 0:
        for _ in range(b):
            next = D[now]
            tmp += now
            now = next

    ans += (N//b) * tmp
    N %= b
    now = c
    for _ in range(N):
        next = D[now]
        ans += now
        now = next
    print(ans)
    exit()
