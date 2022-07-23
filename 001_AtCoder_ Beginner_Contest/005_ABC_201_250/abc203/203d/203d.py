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
sys.setrecursionlimit(500000)
INF = 10**10

# 解説AC
#二分探索を使うというのがわからなかった
#累積和問題という情報は与えられていた

N,K = IIS()
A = LLIIS(N)

ok = INF
ng = -1


def calc(n):
    # 中央値nの区画が存在するか

    D = [[0]*(N+1) for _ in range(N+1)]
    for i , A_ in enumerate(A,start=1):
        for j , a in enumerate(A_,start=1):
            D[i][j] += (n >= a)

    for i in range(N+1):
        for j in range(N):
            D[i][j+1] += D[i][j]

    for j in range(N+1):
        for i in range(N):
            D[i+1][j] += D[i][j]

    #区画を見る
    b = K**2 - (math.floor(K**2 / 2) + 1) + 1
    for i in range(1,N-K+2):
        for j in range(1,N-K+2):
            #区画のn以下の数
            t = D[i+K-1][j+K-1] - D[i+K-1][j-1] - D[i-1][j+K-1] + D[i-1][j-1]
            if b <= t:
                return True
    return False


while (ok-ng) > 1:
    mid = (ok+ng) // 2

    if calc(mid):
        ok = mid
    else:
        ng = mid

print(ok)