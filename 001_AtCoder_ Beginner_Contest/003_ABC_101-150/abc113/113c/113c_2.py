def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


# 座標圧縮
def COMPRESS(arr): return {e: i for i, e in enumerate(sorted(set(arr)))}


N, M = IIS()
query = [LIIS() for _ in range(M)]
comp = [[] for _ in range(N+1)]
for p, y in query:
    comp[p].append(y)

for i in range(N+1):
    comp[i] = COMPRESS(comp[i])

for p, y in query:
    print(str(p).zfill(6) + str(comp[p][y]+1).zfill(6))