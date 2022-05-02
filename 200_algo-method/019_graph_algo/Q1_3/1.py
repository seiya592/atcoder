def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M = IIS()
E =[[] for _ in range(N)]
C = [0] * N

for _ in range(M):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)
    C[a] += 1
    C[b] += 1

a = max(C)

for e in E:
    if a == len(e):
        e.sort()
        print(*e)
        exit()