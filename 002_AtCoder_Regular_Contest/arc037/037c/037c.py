def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import bisect
import math
from decimal import  Decimal
N, K = IIS()
A = LIIS()
B = LIIS()
B.sort()


ng = 0
ok = 10 ** 18 + 1

def check(mid):
    # mid以下の値がK個以上存在するか
    cnt = 0
    for a in A:
        cnt += bisect.bisect_right(B, mid//a)
    if cnt >= K:
        return True
    else:
        return False

while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
