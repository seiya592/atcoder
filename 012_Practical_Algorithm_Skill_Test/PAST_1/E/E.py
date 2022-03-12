def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import copy

# 隣接行列
N, Q = LIIS()
S = [LIIS() for _ in range(Q)]
A = [[False] * (N + 1) for _ in range(N + 1)]

for s in S:
    if s[0] == 1:
        A[s[1]][s[2]] = True
    elif s[0] == 2:
        for i, a in enumerate(A[1:], start=1):
            if a[s[1]] and s[1] != i:
                A[s[1]][i] = True
    else:
        tmp = copy.deepcopy(A)
        for i, t in enumerate(tmp[s[1]][1:], start=1):
            if t:
                for j, x in enumerate(tmp[i][1:], start=1):
                    if x and s[1] != j:
                        A[s[1]][j] = True

for a in A[1:]:
    tmp = ""
    for t in a[1:]:
        if t:
            tmp += 'Y'
        else:
            tmp += 'N'
    print(tmp)
