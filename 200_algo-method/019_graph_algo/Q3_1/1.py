def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M = IIS()
E = [[] for _ in range(N)]
for _ in range(M):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)

from collections import deque

Q = deque()
Q.append(0)
done = [False] * N
ans = [10**10] * N
ans[0] = 0
while len(Q) > 0:
    n = Q.popleft()
    if done[n]:
        continue
    done[n] = True
    for e in E[n]:
        Q.append(e)
        ans[e] = min(ans[e],ans[n]+1)
count = [[] for _ in range(N)]
for i,a in enumerate(ans):
    if a != 10**10:
        count[a].append(i)
for c in count:
    c.sort()
    print(*c)