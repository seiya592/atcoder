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


N = II()
X = []
Y = []
for _ in range(N):
    x,y = IIS()
    X.append(x-y)
    Y.append(x+y)

Xmax = max(X)
Ymax = max(Y)
Xmin = min(X)
Ymin = min(Y)

ans = 0

for x,y in zip(X,Y):
    ans = max(ans, abs(x-Xmax), abs(x-Xmin), abs(y-Ymax), abs(y-Ymin))
print(ans)