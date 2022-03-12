def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()
ALL = 2 ** N
A = [0]
C = [0]
for i in range(M):
    a, b = IIS()
    t = LIIS()
    value = 0
    for tt in t:
        value += 1 << (tt - 1)
    C.append(value)
    A.append(a)

INF = 10 ** 100
cost = [[INF]*(ALL) for _ in range(M+1)]
cost[0][0] = 0
for i in range(1,M+1):
    for j in range(ALL):
        cost[i][j] = min(cost[i][j],cost[i-1][j])
        cost[i][j|C[i]] = min(cost[i][j|C[i]] , cost[i-1][j]+A[i])

ans = cost[M][ALL-1] if cost[M][ALL-1] != INF else -1
print(ans)
