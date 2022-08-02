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


N = II()
A = LI(N)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i][j] == 'W' and A[j][i] == 'L':
            continue
        if A[i][j] == 'L' and A[j][i] == 'W':
            continue
        if A[i][j] == 'D' and A[j][i] == 'D':
            continue
        print('incorrect')
        exit()
print('correct')