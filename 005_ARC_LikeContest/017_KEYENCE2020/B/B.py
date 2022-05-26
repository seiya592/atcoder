def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]
INF = 10**20


N = II()
X = []
for _ in range(N):
    x, l = IIS()
    X.append((x-l ,x+l))

X.sort(key=lambda x:x[1])

now = -10**10
ans = 0
for s, e in X:
    if now <= s:
        ans += 1
        now = e
print(ans)