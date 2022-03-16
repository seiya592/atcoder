def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()
INF = 10**100
dict = [[INF] * N for _ in range(N)]


for _ in range(M):
    a,b,t = IIS()
    dict[a-1][b-1] = t
    dict[b-1][a-1] = t

for i in range(N):
    dict[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dict[i][j] = min(dict[i][j],dict[i][k]+dict[k][j])
ans = INF
for d in dict:
    ans = min(ans,max(d))
print(ans)