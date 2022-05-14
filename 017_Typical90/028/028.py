def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
ALL = 1000

S = [[0] * (ALL+1) for _ in range(ALL+1)]

for _ in range(N):
    lx, ly, rx, ry = IIS()
    #左上
    S[lx][ry] -= 1

    #右下
    S[rx][ly] -= 1

    #左下
    S[lx][ly] += 1

    #右上
    S[rx][ry] += 1

for i in range(ALL+1):
    for j in range(1,ALL+1):
        S[i][j] += S[i][j-1]

for i in range(1, ALL+1):
    for j in range(ALL+1):
        S[i][j] += S[i-1][j]

ans = [0] * N
for i in range(ALL+1):
    for j in range(ALL+1):
        if S[i][j]:
            ans[S[i][j]-1] += 1

for a in ans:
    print(a)