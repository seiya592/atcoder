"""
2023/03/04 20:57:14
"""
import collections


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
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')        
sys.setrecursionlimit(500000)
INF = 10**17


N,M = IIS()
E = [[] for _ in range(N+1)]
V = [0] * (N+1)

for _ in range(M):
    x,y = IIS()
    E[x].append(y)
    V[y] += 1

Q = collections.deque()
for i,v in enumerate(V[1:],start=1):
    if not v:
        Q.append(i)
ans = [0] * (N+1)
now = 1
while Q:
    if len(Q) != 1:
        NO()
    n = Q.popleft()
    if ans[n] != 0:
        NO()
    ans[n] = now
    now += 1

    for e in E[n]:
        V[e] -= 1
        if not V[e]:
            Q.append(e)
print('Yes')
print(*ans[1:])