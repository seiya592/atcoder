def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import bisect

N = II()
A = LIIS()
A.sort()
Q = II()
B = []
for _ in range(Q):
    B = II()
    i = bisect.bisect_left(A, B)
    tmp1 = A[min(i, N-1)]
    tmp2 = A[max(0, i-1)]
    print(min(abs(B-tmp1), abs(B-tmp2)))
