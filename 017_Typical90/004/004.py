def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


H, W = IIS()
A = [LIIS() for _ in range(H)]
A_r = [l for l in zip(*A)]

A_sum_row = [sum(l) for l in A_r]
A_sum_col = [sum(l) for l in A]

ans = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans[i][j] = str(A_sum_col[i] +  A_sum_row[j] - A[i][j])

for a in ans:
    print(" ".join(a))
