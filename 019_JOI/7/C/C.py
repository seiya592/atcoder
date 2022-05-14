def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M = IIS()
P = [0]
for _ in range(N):
    a = II()
    P.append(a)

# あらかじめ計算しておく
PP = []
for i in range(N+1):
    for j in range(N+1):
        PP.append(P[i]+P[j])

PP.sort()

ans = 0
import bisect
for p in PP:
    t = p
    t += PP[bisect.bisect_right(PP,M-t) - 1]
    if t <= M:
        ans = max(ans,t)
print(ans)