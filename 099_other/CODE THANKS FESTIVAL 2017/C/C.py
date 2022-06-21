import heapq


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


# https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_c

N, K = IIS()

Q = []
heapq.heapify(Q)

for _ in range(N):
    a,b = IIS()
    heapq.heappush(Q,(a,b))

ans = 0
while K:
    a,b = heapq.heappop(Q)
    ans += a
    heapq.heappush(Q,(a+b,b))
    K -= 1

print(ans)