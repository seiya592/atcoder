def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
P1 = [0] * (N + 1)
P2 = [0] * (N + 1)

for i in range(1, N+1):
    c, p = IIS()
    if c == 1:
        P1[i] = P1[i-1] + p
        P2[i] = P2[i-1]
    else:
        P1[i] = P1[i - 1]
        P2[i] = P2[i - 1] + p

Q = II()
for i in range(Q):
    L, R = IIS()
    print(P1[R] - P1[L-1], P2[R] - P2[L-1])