"""
2022/10/31 19:00:35
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


N,M = IIS()
XYZ = LLIIS(N)

def calc(a,b,c):
    ans = 0
    Q = []
    heapq.heapify(Q)
    for x,y,z in XYZ:
        heapq.heappush(Q,-(a*x+b*y+c*z))
    now = M
    while now:
        ans += heapq.heappop(Q)
        now -= 1
    return -ans

ans = -INF
for a in [-1,1]:
    for b in [-1,1]:
        for c in [-1,1]:
            ans = max(ans, calc(a,b,c))
print(ans)