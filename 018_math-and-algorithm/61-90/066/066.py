"""
2022/08/09 21:25:06
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
INF = 10**10


N, K = IIS()

ans = N ** 3

for i in range(1,N+1):
    for j in range(max(1,i-(K-1)), min(i+(K-1)+1,N+1)):
        for k in range(max(1,j-(K-1)), min(j+(K-1)+1,N+1)):
            if abs(i-k) < K:
                ans -= 1
print(ans)