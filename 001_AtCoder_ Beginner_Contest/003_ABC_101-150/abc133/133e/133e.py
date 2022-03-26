def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
from collections import deque

N, K = IIS()
E = [[] for _ in range(N+1)]
f = [True] * (N+1)
for _ in range(N-1):
    a, b = IIS()
    E[a].append(b)
    E[b].append(a)


def dfs(old,next,pattern):
    f[next] = False
    used = 1
    ret = pattern
    if old != 0:
        used += 1
    for e in E[next]:
        if next != e and f[e]:
            ret *= dfs(next, e, K - used)
            ret %= 10**9 + 7
            used += 1
    return ret

print(dfs(0, 1, K))