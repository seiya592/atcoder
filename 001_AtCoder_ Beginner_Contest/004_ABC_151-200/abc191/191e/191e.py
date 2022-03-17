from collections import defaultdict

N, M = map(int, input().split())

d = defaultdict(dict)
for i in range(M):
    A, B, C = map(int, input().split())
    tmpD = {A: C}
    if not A in d[B] or d[B][A] > C:
        d[B].update(tmpD)

print(d)
