def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N,M,Q = IIS()
LR = LLIIS(M)
PQ = LLIIS(Q)

# 二次元累積和
total = [[0] * (N+2) for _ in range(N+2)]

# プロット
for l, r in LR:
    total[l][r] += 1

# 二次元累積和
for i in range(1, N+1):
    for j in range(1, N+1):
        total[i][j] += total[i][j-1]

    for j in range(1, N+1):
        total[i][j] += total[i-1][j]

for p,q in PQ:
    print(total[q][q] - total[p-1][q] - total[q][p-1] + total[p-1][p-1])