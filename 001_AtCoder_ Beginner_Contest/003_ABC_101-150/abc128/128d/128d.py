"""
2022/10/25 17:38:39
"""
import heapq


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
from functools import lru_cache

N,K = IIS()
V = LIIS()

@lru_cache(maxsize=10000)
def calc(l,r):
    if l + r > N:
        return 0
    if l+r > K:
        return 0

    ans = max(calc(l+1,r), calc(l,r+1))

    Q = []
    heapq.heapify(Q)
    t = 0
    for i in range(l):
        heapq.heappush(Q,V[i])
        t += V[i]
    for i in range(N-1, N-1-r,-1):
        heapq.heappush(Q,V[i])
        t += V[i]

    k = K-l-r
    while k and Q:
        p = heapq.heappop(Q)
        if p >= 0:
            break
        t -= p
        k -= 1

    return max(ans,t)

print(calc(0,0))