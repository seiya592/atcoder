"""
2022/08/06 20:52:01
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


N, M = IIS()
v = []
def dfs(now, num):
    global v
    if now == N:
        print(*v)
        return

    for i in range(num,M+1):
        v.append(i)
        dfs(now+1, i+1)
        v = v[:-1]

dfs(0,1)
