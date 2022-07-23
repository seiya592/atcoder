def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(): return [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
A = LLIIS(N)
ans = 0
for i in range(N):
    for j in range(N):
        for x,y in PLUS():
            tmp = 0
            for n in range(N):
                tmp *= 10
                tmp += int(A[(i+(x*n))%N][(j+(y*n))%N])
            ans = max(tmp,ans)
print(ans)