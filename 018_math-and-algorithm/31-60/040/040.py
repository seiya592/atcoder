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
INF = 10**10


N = II()
A = LIIS()
T = [0] * 2
for a in A:
    T.append(T[-1] + a)

M = II()
now = II()
ans = 0
for _ in range(M-1):
    b = II()
    x,y = max(now,b), min(now,b)
    ans += T[x] - T[y]
    now = b
print(ans)