def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,X = IIS()
A = LIIS()


def dfs(n):
    if n == 0:
        return 0

    return dfs(A[n-1]) + 1
print(dfs(X))