def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N,K,Q = IIS()
A = IIS()
L =IIS()

ans = [False] * (N+1)

for a in A:
    ans[a] = True

for q in L:

    cnt = 0
    for i,a in enumerate(ans):
        if a:
            cnt += 1
        if q == cnt:
            t = i
            break

    if t == N:
        continue
    if ans[t] and not ans[t+1]:
        ans[t] = False
        ans[t+1] = True

ans2 = []
for i in range(N+1):
    if ans[i]:
        ans2.append(i)
print(*ans2)