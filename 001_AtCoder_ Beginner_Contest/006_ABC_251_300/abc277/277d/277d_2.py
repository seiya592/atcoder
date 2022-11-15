"""
2022/11/13 13:45:21
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N,M = IIS()
A = LIIS()

A.sort()
A_sum = sum(A)
ans = []


old = -INF
tot = 0
i = 0
while i < N:
    if old == A[i] or old + 1 == A[i]:
        tot += A[i]
    else:
        ans.append(tot)
        tot = A[i]
    old = A[i]
    i += 1
else:
    ans.append(tot)

if A[0] == 0 and A[-1] == M-1 and len(ans) > 2:
    ans.append(ans[1]+ans[-1])

print(A_sum-max(ans))