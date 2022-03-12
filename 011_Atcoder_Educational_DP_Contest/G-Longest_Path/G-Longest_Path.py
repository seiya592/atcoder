def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(100000000)

N, M = IIS()
edgs = [[] for _ in range(N + 1)]   # 0は無視
length = [-1] * (N + 1)
start = [True] * (N + 1)
for i in range(M):
    x,y = IIS()
    edgs[x].append(y)
    start[y] = False


def dfs(i):
    if length[i] != -1:
        return length[i]
    length[i] = 0
    for e in edgs[i]:
        length[i] = max(length[i], dfs(e) + 1)
    return length[i]

for i in range(1, N + 1):
    if start[i]:
        dfs(i)

print(max(length))