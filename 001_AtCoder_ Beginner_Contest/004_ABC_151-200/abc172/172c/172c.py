def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)
import bisect

N, M, K = IIS()

A = LIIS()
B = LIIS()

A_s = [0]
f = True
for a in A:
    A_s.append(A_s[-1] + a)

B_s = [0]
for b in B:
    B_s.append(B_s[-1] + b)

ans = 0
for i, a in enumerate(A_s):
    if a > K:
        break
    t = K - a
    j = bisect.bisect_right(B_s,t)-1
    ans = max(ans,i+j)
print(ans)