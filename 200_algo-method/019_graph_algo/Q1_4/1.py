def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M,X = IIS()
E =[[] for _ in range(N)]

for _ in range(M):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

ans = set()
ans.add(X)
for e in E[X]:
    ans.add(e)
    for ee in E[e]:
        ans.add(ee)

print(len(ans) - len(E[X])-1)