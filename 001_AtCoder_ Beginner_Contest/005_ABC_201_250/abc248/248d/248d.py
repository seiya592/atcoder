def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
import bisect

N = II()
A = LIIS()
Q = II()
num = [[] for _ in range(N+1)]  #Aiの値が入っていた場所
for i,a in enumerate(A,start=1):
    num[a].append(i)

for _ in range(Q):
    L,R,X = IIS()
    if num[X]:
        L_i = bisect.bisect_left(num[X], L)
        R_i = bisect.bisect_right(num[X], R)
        print(R_i - L_i)
    else:
        print(0)