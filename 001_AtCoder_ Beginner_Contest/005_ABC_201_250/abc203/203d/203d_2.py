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
A = LLIIS(N)


def calc(n):
    S = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            S[i+1][j+1] = (A[i][j] > n)

    for i in range(1,N+1):
        for j in range(1, N+1):
            S[i][j] += S[i][j-1]

    for j in range(1,N+1):
        for i in range(1, N+1):
            S[i][j] += S[i-1][j]

    B = ((K**2) // 2) + 1
    for i in range(K,N+1):
        for j in range(K,N+1):
            if S[i][j] - S[i-K][j] - S[i][j-K] + S[i-K][j-K] < B:
                return True
    return False


ok = 10**9+1
ng = -1

while (ok-ng) > 1:
    mid = (ok+ng) // 2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok)