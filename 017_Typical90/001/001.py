def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import bisect

N, L = IIS()
K = II()
A = LIIS() + [L]

ng = L + 1
ok = 0

def check(n):
    # AをK回分割したときにn[cm]以上で区切れるか
    c = n
    for _ in range(K+1):
        i = bisect.bisect_left(A,c)
        if len(A) == i:
            return False
        c = A[i] + n
    return True

while abs(ok-ng)>1:
    mid = (ok+ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)