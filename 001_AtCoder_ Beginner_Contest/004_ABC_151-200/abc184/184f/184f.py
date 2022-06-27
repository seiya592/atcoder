def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import bisect
def has_bit(n, i):
    return (n & (1<<i)) > 0

N, T = IIS()
tmp = LIIS()
A = []
B = []
for i, t in enumerate(tmp):
    if i % 2 == 0:
        A.append(t)
    else:
        B.append(t)

ALL = 2 ** N

C = []
for i in range(2 ** len(A)):
    tmp = 0
    for j in range(len(A)):
        if has_bit(i,j):
            tmp += A[j]
    C.append(tmp)

C.sort()
ans = [0]
for i in range(2** len(B)):
    tmp = 0
    for j in range(len(B)):
        if has_bit(i,j):
            tmp += B[j]
    Tmax = T - tmp
    k = bisect.bisect_right(C,Tmax) -1
    if k == -1:
        k = 0
    if k == len(C):
        k -= 1
    ans.append(tmp+ C[k])

ans.sort()
i = bisect.bisect_right(ans, T) -1
if -1 == i:
    i = 0
print(ans[i])
pass
