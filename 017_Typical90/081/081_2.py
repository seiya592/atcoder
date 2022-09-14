def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, K = IIS()
M = 5000
S = [[0] * (M+1) for _ in range(M+1)]

# 身長a 体重b　の人の数をカウント
for _ in range(N):
    a,b = IIS()
    S[a][b] += 1

for i in range(1,M+1):
    for j in range(1,M+1):
        S[i][j] += S[i][j-1]

for j in range(1,M+1):
    for i in range(1, M+1):
        S[i][j] += S[i-1][j]

ans = 0
for i in range(0+K+1, M+1):
    for j in range(0+K+1, M+1):
        ans = max(ans, S[i][j] - S[i-K-1][j] - S[i][j-K-1] + S[i-K-1][j-K-1])
print(ans)