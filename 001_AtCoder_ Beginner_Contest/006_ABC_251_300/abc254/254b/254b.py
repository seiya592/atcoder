def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10


N = II()
old = []
for i in range(N):
    now = []
    for j in range(i+1):
        if j == 0 or j == i:
            now.append(1)
        else:
            now.append(old[j-1]+old[j])
    old = now
    print(*now)