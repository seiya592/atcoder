"""
2022/10/22 20:58:13
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N = II()
A = LIIS()

E = [[] for _ in range(N*2+1+1)]

for i, a in enumerate(A,start=1):
    E[a].append(i*2)
    E[a].append(i*2+1)

ans = [-INF] * (2*N+1+1)
def dfs(n,d):
    ans[n] = d

    for e in E[n]:
        if ans[n] != -INF:
            dfs(e, d+1)
dfs(1,0)
for a in ans[1:]:
    print(a)