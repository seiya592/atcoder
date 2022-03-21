def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import bisect

N, M = IIS()
A = LIIS()

ch = [0] * N

for a in A:
    i = bisect.bisect_right(ch,-a)
    if i != N:
        print(i + 1)
        ch[i] = -a
    else:
        print(-1)

