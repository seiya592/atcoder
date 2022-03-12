def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
def has_bit(n, i):
    return (n & (1<<i)) > 0

N, M, X = IIS()
C = []
A = []

for i in range(N):
    t = LIIS()
    C.append(t[0])
    A.append(t[1:])

ALL = 2 ** N
ans = 10 ** 100
for n in range(ALL):
    cost = 0
    skill = [0] * M
    for i in range(N):
        if has_bit(n,i):
            cost += C[i]
            for j in range(M):
                skill[j] += A[i][j]
    if all(k >= X for k in skill):
        ans = min(ans, cost)

if ans == 10 ** 100:
    ans = -1
print(ans)
