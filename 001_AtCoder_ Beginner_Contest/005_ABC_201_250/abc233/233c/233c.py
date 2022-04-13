def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)
from functools import lru_cache

N, X = IIS()
L = LLIIS(N)
ans = 0

@lru_cache(maxsize=10000)
def dfs(i,n):
    ret = 0
    if i == N:
        if n == 1:
            return 1
        return 0
    for l in L[i][1:]:
        if n % l == 0:
            ret += dfs(i+1, n//l)
    return ret


for l in L[0][1:]:
    if X % l == 0:
        ans += dfs(1, X//l)
print(ans)