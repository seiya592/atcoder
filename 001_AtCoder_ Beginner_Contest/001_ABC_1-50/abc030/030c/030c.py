def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
import bisect

N, M = IIS()
X,Y = IIS()
A = LIIS()
B = LIIS()

x = 0
y = 0
now = 0
Aflg = True
ans = 0
while x < N and y < M:
    if Aflg:
        if now <= A[x]:
            Aflg ^= 1
            now = X + A[x]
        else:
            x += 1
    else:
        if now <= B[y]:
            Aflg ^= 1
            now = Y + B[y]
            ans += 1
        else:
            y += 1
print(ans)