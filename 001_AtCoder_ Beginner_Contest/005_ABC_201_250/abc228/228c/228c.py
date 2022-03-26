def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, K = IIS()
P = []
for _ in range(N):
    p1,p2,p3 = IIS()
    P.append(sum([p1,p2,p3]))

Ps = sorted(P, reverse=True)
border = Ps[K-1]

for p in P:
    if border <= p + 300:
        print('Yes')
    else:
        print('No')

