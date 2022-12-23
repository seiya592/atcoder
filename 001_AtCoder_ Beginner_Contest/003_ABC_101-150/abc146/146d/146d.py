"""
2022/11/25 22:04:22
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
E = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b = IIS()
    E[a].append((b,i))
    E[b].append((a,i))

ans = [0] * (N-1)

def dfs(n,o,o_c):

    color = 1
    for e,i in E[n]:
        if e == o:
            continue
        if color == o_c:
            color += 1
        ans[i] = color
        dfs(e,n,color)
        color += 1

dfs(1,0,0)
print(max(ans))
for a in ans:
    print(a)