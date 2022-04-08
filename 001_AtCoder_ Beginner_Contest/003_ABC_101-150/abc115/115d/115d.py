def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)

N, X = IIS()

T = [0] * (N+1)
P = [0] * (N+1)
T[0] = 1
P[0] = 1

for i in range(1,N+1):
    T[i] = 3 + (T[i-1] * 2)
    P[i] = 1 + (P[i-1] * 2)

ans = 0

def dfs(n, x):
    global ans
    if x < X:
        x += 1
    else:
        print(ans)
        exit()

    if x + T[n-1] <= X:
        x += T[n-1]
        ans += P[n-1]
    else:
        dfs(n-1, x)

    if x < X:
        x += 1
        ans += 1
    else:
        print(ans)
        exit()

    if x + T[n-1] <= X:
        x += T[n-1]
        ans += P[n-1]
    else:
        dfs(n-1, x)

    if x < X:
        x += 1
    else:
        print(ans)
        exit()

dfs(N, 0)
print(ans)

