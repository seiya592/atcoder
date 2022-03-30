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
B = LIIS()
C = LIIS()
A.sort()
B.sort()
C.sort()

# B-C間の組み合わせを数える
BC = [0] * N
tmp = 0
for n, b in enumerate(reversed(B)):
    i = bisect.bisect_right(C,b)
    tmp += len(C) - i
    BC[N-n-1] = tmp

ans = 0
for n, a in enumerate(A):
    i = bisect.bisect_right(B, a)
    if i != len(BC):
        ans += BC[i]
print(ans)