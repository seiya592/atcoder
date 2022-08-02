import copy
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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, M = IIS()
A = LIIS()

Q = []
for a in A:
    Q.append(-a)

heapq.heapify(Q)

while M:
    n = abs(heapq.heappop(Q))
    heapq.heappush(Q,-(n//2))
    M -= 1
print(abs(sum(Q)))