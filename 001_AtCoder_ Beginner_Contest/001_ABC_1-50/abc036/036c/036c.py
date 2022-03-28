def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

# 座標圧縮
def COMPRESS(arr): return {e: i for i, e in enumerate(sorted(set(arr)))}

N = II()
A = []
for _ in range(N):
    A.append(II())

comp = COMPRESS(A)

for a in A:
    print(comp[a])
