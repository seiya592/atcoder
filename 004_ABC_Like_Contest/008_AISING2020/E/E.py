"""
2022/10/29 2:38:08
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


for _ in range(II()):
    N = II()

    E = [[] for _ in range(N+1)]        # 左に居たい牛
    R = [[] for _ in range(N+1)]        # 右に居たい牛
    ans = 0
    for _ in range(N):
        k,l,r = IIS()

        # 最低限の値
        if l - r >= 0:
            ans += r
            E[k].append(l-r)    # k番目以内に入らなかったらl-r分ansが増える
        else:
            ans += l
            R[k].append(r-l)


    Q = []
    heapq.heapify(Q)

    for i in range(1,N+1):
        for e in E[i]:
            ans += e
            heapq.heappush(Q,e)

        while len(Q) > i:
            t = heapq.heappop(Q)
            ans -= t

    Q = []
    heapq.heapify(Q)
    for i in range(N-1,0,-1):
        for r in R[i]:
            ans += r
            heapq.heappush(Q,r)

        while len(Q) > N - i:
            t = heapq.heappop(Q)
            ans -= t

    print(ans)
