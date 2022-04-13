def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()

def dfs(n):
    if n == 1:
        ans.append(n)
        return '1'
    dfs(n-1)
    ans.append(n)
    dfs(n-1)


ans = []
dfs(N)
for a in ans:
    print(a, end=' ')
print()