import bisect


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
S = I()
W = LIIS()

ad = []
cr = []

for w,s in zip(W,S):
    if s == '0':
        cr.append(w)
    else:
        ad.append(w)

cr.sort()
ad.sort()
ans = 0
for w in W+[0,INF]:
    #wを閾値にセット
    c = bisect.bisect_left(cr,w)
    a = len(ad) - bisect.bisect_right(ad,w-1)
    ans = max(ans,c+a)
print(ans)