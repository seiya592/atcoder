def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
from functools import lru_cache
sys.setrecursionlimit(1000010)


N,K = IIS()
H = LIIS()

#メモ化再帰
# @lru_cache(maxsize=1000010)
memo = [10**10] * N
def dfs(n):
    if n == 0:
        return 0
    if memo[n] != 10**10:
        return memo[n]
    c = 10 ** 10
    for k in range(n-1,max(n-K-1,-1),-1):
        c = min(c,dfs(k)+ abs(H[k]-H[n]))
    memo[n] = c
    return c

print(dfs(N-1))