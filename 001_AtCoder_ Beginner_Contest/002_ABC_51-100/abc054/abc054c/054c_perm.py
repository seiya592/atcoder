import itertools
def IIS(): return map(int, input().split())

N,M = IIS()
E = [[False]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = IIS()
    E[a][b] = True
    E[b][a] = True
ans = 0
for p in itertools.permutations(range(2,N+1)):
    p = list(p) + [1]
    if not all([E[p[i]][p[i+1]] for i in range(N-1)]):
        continue    # １つでも辺が繋がっていなかったらNG
    ans += 1
print(ans)