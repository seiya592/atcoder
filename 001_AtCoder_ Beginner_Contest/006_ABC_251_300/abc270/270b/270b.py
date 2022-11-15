"""
2022/09/24 20:50:54
"""
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


X,Y,Z = IIS()
if 0<Y<X:
    #ハンマーいる
    if Y<Z:
        #ハンマー取れない
        print(-1)
        exit()
    if 0 < Z:
        #ハンマーが経路上にある
        print(abs(X))
        exit()
    else:
        print(abs(Z)*2 + abs(X))
        exit()
elif X<Y<0:
    #ハンマーいる
    if Z<Y:
        #ハンマー取れない
        print(-1)
        exit()
    if Z < 0:
        #ハンマーが経路上にある
        print(abs(X))
        exit()
    else:
        print(abs(Z) * 2 + abs(X))
        exit()

else:
    #ハンマーいらない
    print(abs(X))
    exit()