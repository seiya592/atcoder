#　隣接リスト
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

N, M, Q = LIIS()
v = [LIIS() for _ in range(M)]
c = [0] + LIIS()
S = [LIIS() for _ in range(Q)]

G = []
for _ in range(N + 1):
    G.append([])


for v1, v2 in v:
    G[v1].append(v2)
    G[v2].append(v1)

for s in S:
    if s[0] == 1:
        color = c[s[1]]
        print(color)
        for g in G[s[1]]:
            c[g] = color

    else:
        print(c[s[1]])
        c[s[1]] = s[2]