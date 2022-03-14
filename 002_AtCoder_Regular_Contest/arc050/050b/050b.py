def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


R, B = IIS()
x, y = IIS()

ok = 0
ng = 10 ** 18

while abs(ng-ok) > 1:
    mid = (ok + ng) // 2

    # mid個作る場合 最低各種1本は必要
    r = R - mid
    b = B - mid

    if r < 0 or b < 0:
        ng = mid
    else:
        tmp = (r // (x-1)) + (b // (y-1))
        if tmp < mid:
            ng = mid
        else:
            ok = mid

print(ok)