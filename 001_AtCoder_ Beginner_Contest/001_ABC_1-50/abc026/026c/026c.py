def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(100000000)

N = II()
child = [[] for _ in range(N + 1)]   # 0は無視

for i in range(2,N+1):
    m = II()
    child[m].append(i)


def dfs(m):
    if not child[m]:
        return 1

    value = []
    for i in child[m]:
        value.append(dfs(i))

    if len(child[m]) == 1:
        return value[0] * 2 + 1
    else:
        return max(value) + min(value) + 1

print(dfs(1))