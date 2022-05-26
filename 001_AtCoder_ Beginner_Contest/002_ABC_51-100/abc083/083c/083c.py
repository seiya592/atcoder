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


X,Y = IIS()

ans = 0
while X <= Y:
    ans += 1
    X *= 2
print(ans)