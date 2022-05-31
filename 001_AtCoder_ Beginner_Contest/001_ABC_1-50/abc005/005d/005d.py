def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
D = LLIIS(N)
Q = II()
P = [II() for _ in range(Q)]

# 長方形の累積和
S = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1, N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] + D[i-1][j-1] - S[i-1][j-1]


size = [0] * (N**2 + 1)
for x1 in range(1,N+1):
    for x2 in range(x1,N+1):
        for y1 in range(1, N+1):
            for y2 in range(y1,N+1):
                s = (x2-(x1-1)) * (y2-(y1-1))
                size[s] = max(size[s], S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1])

for i in range(1,len(size)):
    size[i] = max(size[i-1],size[i])

for p in P:
    print(size[p])