def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, Q = IIS()
Query = []
for _ in range(Q):
    q = II()
    Query.append(q)

A = [0] * (N+1)
B = [0] * (N+1)
#A = 場所iのボールの値
#B = 値iの場所

for i in range(N+1):
    A[i] = i
    B[i] = i

for q in Query:
    a = B[q]    #値qの場所
    if a == N:
        a -= 1
    A[a + 1], A[a] = A[a], A[a+1]   #入れ替え
    B[q] = a+1
    B[A[a]] = a
print(*A[1:])