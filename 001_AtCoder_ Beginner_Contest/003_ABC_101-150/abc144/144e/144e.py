"""
2022/09/09 17:36:53
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
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N, K = IIS()
A = LIIS()
F = LIIS()
A.sort()
F.sort(reverse=True)

ok = INF
ng = -1

def calc(B):
    c = 0
    for a,f in zip(A,F):
        c += max(a - (B // f), 0)
    if c <= K:
        return True
    return False

while(ok-ng) > 1:
    mid = (ok+ng) // 2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok)