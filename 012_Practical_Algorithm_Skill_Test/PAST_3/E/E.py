# 隣接行列
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))


N, M, Q = LIIS()
v = [LIIS() for _ in range(M)]
c = [0] + LIIS()
S = [LIIS() for _ in range(Q)]

g = [([False] * (N + 1)) for _ in range(N + 1)]

for v1, v2 in v:
    g[v1][v2] = True
    g[v2][v1] = True

for s in S:
    if s[0] == 1:
        color = c[s[1]]
        print(color)
        for i, t in enumerate(g[s[1]]):
            if t:
               c[i] = color
    else:
        print(c[s[1]])
        c[s[1]] = s[2]
