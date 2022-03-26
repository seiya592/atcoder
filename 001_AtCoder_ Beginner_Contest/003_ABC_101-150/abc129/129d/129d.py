def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


H, W = IIS()
S = [list(I()) for _ in range(H)]
Sr = [l for l in zip(*S)]

col_LMP = [[-1]*W for _ in range(H)]

for i, s in enumerate(S):
    st = 0
    for j in range(W):
        if S[i][j] == '#':
            for k in range(st,j):
                col_LMP[i][k] = j - st
            st = j + 1
    else:
        for k in range(st, W):
            col_LMP[i][k] = W - st

ans = [[-1] * W for _ in range(H)]

for j, s in enumerate(Sr):
    st = 0
    for i in range(H):
        if Sr[j][i] == '#':
            for k in range(st, i):
                ans[k][j] = (col_LMP[k][j] - 1) + (i - st)
            st = i + 1
    else:
        for k in range(st, H):
            ans[k][j] = (col_LMP[k][j] - 1) + (H - st)

ansP = 0
for a in ans:
    ansP = max(ansP, max(a))

print(ansP)