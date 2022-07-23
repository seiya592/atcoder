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

# 解説AC
# なんか素数列挙関数使ってTLEしてた（使う必要ない）

N, K = IIS()
ans = [0] * (N+1)

for p in range(2,N+1):
    if ans[p]:
        continue
    for i in range(p,N+1,p):
        ans[i] += 1

print(sum([(a>=K) for a in ans]))