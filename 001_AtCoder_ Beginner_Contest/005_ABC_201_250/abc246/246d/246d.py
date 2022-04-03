def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()

def func(a, b):
    return a**3 + (a**2 * b) + (a * b**2) + b**3

ok = 10 ** 10
ng = 0

if N == 0:
    print(0)
    exit()

while abs(ok- ng) > 1:
    mid = (ok+ng) // 2
    if N <= func(mid, mid):
        ok = mid
    else:
        ng = mid

ans = func(ok,ok)
up = ok
down = ok

while True:

    if down < 0:
        print(ans)
        exit()
    tmp2 = func(up, down)
    if tmp2 >= N:
        ans = min(ans, tmp2)
        down -=1
        flg = False
    else:
        if flg:
            print(ans)
            exit()
        flg = True
        up += 1

# print(ok)
# print(func(ok, ok))