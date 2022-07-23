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


N = II()
X = []
Y = []
for _ in range(N):
    x,y = IIS()
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()

a = X[N//2]
b = Y[N//2]

ans = 0
for x, y in zip(X, Y):
    ans += abs(x-a) + abs(y-b)

print(ans)
