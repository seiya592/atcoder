def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)
# 解説読み

N, X, Y = IIS()
A = LIIS()

#　包除原理
# XYが含まれている組み =　X以下、Y以上がない配列の組み  - Xが含まない組  - Yが含まれない組  + XYが含まれない組

XYall = [True] * N     #X以下、Y以上がない配列の組み
nX = [True] * N        #Xが含まない組(X以下、Y以上がない前提)
nY = [True] * N        #Yが含まれない組(X以下、Y以上がない前提)
nXnY = [True] * N      #XYが含まれない組(X以下、Y以上がない前提)

for i, a in enumerate(A):
    if X < a or Y > a:
        XYall[i] = False
        nX[i] = False
        nY[i] = False
        nXnY[i] = False
    if X == a:
        nX[i] = False
        nXnY[i] = False
    if Y == a:
        nY[i] = False
        nXnY[i] = False

def f(lst):
    c = 1
    ret = 0
    for b in lst:
        if b:
            c += 1
        else:
            ret += (c * (c-1)) // 2
            c = 1
    else:
        ret += (c * (c - 1)) // 2
    return ret

print(f(XYall) - f(nX) - f(nY) + f(nXnY))