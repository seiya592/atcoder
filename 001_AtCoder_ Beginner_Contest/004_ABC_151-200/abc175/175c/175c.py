def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


X, K, D = IIS()
m = abs(X) // D
if K >= m:
    d = K - m
    if X < 0:
        x = X + (m * D)
        if d % 2 == 0:
            print(abs(x))
        else:
            print(abs(x+D))
    else:
        x = X - (m * D)

        if d % 2 == 0:
            print(abs(x))
        else:
            print(abs(x-D))
else:
    if X < 0:
        print(abs(X + (K * D)))
    else:
        print(abs(X - (K * D)))
