def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


import bisect

A, B, X = IIS()
ok = 0
ng = 10 ** 9 + 1

while abs(ok-ng) > 1:
    mid = (ok + ng) // 2
    if X >= (A*mid + B*(len(str(mid)))):
        ok = mid
    else:
        ng = mid

print(ok)

