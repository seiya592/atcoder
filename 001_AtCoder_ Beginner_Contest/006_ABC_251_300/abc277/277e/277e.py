"""
2022/11/12 20:42:26
"""
import collections


def I(): return input().rstrip()


def IS(): return input().split()


def II(): return int(input())


def IIS(): return map(int, input().split())


def LIIS(): return list(map(int, input().split()))


def LLIIS(n): return [LIIS() for _ in range(n)]


def LI(n): return [I() for _ in range(n)]


def PLUS(x, y): return [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]


def YES(): print('Yes'), exit()


def NO(): print('No'), exit()


def CEIL(x, y): return -(-x // y)  # 除算を小数点切り上げ


import sys

sys.setrecursionlimit(500000)
INF = 10 ** 17

N, M, K = IIS()

ON = [[] for _ in range(N + 1)]
OFF = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, a = IIS()
    if a:
        ON[v].append(u)
        ON[u].append(v)
    else:
        OFF[u].append(v)
        OFF[v].append(u)

S = set(map(int, input().split()))

Q = collections.deque()
Q.append((1, 1, 0))
# n,switch,dist

dist_on = [INF] * (N + 1)
dist_off = [INF] * (N + 1)
ans = INF

while Q:
    n, s, d = Q.popleft()

    if n == N:
        ans = min(ans, d)

    if s or n in S:
        # SWがON
        if dist_on[n] <= d:
            continue
        dist_on[n] = d

        for e in ON[n]:
            if dist_on[e] <= d + 1:
                continue
            Q.append((e, 1, d + 1))
    if not s or n in S:
        # SWがOFF
        if dist_off[n] <= d:
            continue
        dist_off[n] = d

        for e in OFF[n]:
            if dist_off[e] <= d + 1:
                continue
            Q.append((e, 0, d + 1))
print(ans if ans != INF else -1)