"""
2022/09/24 20:51:07
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


N,K = IIS()
A = LIIS()

ok = 0
ng = max(A) + 1

def calc(n):
    # n周した時にりんごを食べた総数がK未満か
    t = 0
    for a in A:
        t += min(n,a)

    return (K > t)

while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    if calc(mid):
        ok = mid
    else:
        ng = mid

t = 0
ans = []
for i in range(N):
    t += min(A[i],ok)
    A[i] = max(A[i]-ok,0)

for a in A:
    if t < K and a > 0:
        t += 1
        ans.append(a-1)
    else:
        ans.append(a)

print(*ans)