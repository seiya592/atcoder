def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M, Q = IIS()
ABCD = [LIIS() for _ in range(Q)]

ans = 0
A = [-1] * (N + 1)  # 最初の桁は無視
A[0] = 1
def dfs(i):
    global ans
    if i == (N+1):
        tmp = 0
        for a,b,c,d in ABCD:
            if A[b] - A[a] == c:
                tmp += d
        ans = max(ans,tmp)
    else:
        for j in range(A[i-1],(M+1)):
            A[i] = j
            dfs(i+1)

for i in range(1,(M+1)):
    A[0] = i
    dfs(1)
print(ans)