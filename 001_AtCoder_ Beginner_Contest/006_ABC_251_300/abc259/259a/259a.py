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


N,M,X,T,D = IIS()

ans = []
for i in range(X+1):
    ans.append(i*D)

for _ in range(X,N+1):
    ans.append(ans[-1])
print(T - (ans[-1] - ans[M]))
