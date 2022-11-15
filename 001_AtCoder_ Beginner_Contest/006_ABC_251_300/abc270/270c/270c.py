"""
2022/09/24 20:50:58
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


N,X,Y = IIS()
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = IIS()
    E[u].append(v)
    E[v].append(u)

ans = [0] * (N+1)    #経路を保存
p = 0
def dfs(n,o):
    global p
    global ans
    ans[p] = n
    p += 1

    if n == Y:
        ans.append(n)
        print(*ans[:p])
        exit()

    for e in E[n]:
        if e == o:
            continue
        dfs(e,n)

    p -= 1


dfs(X,0)