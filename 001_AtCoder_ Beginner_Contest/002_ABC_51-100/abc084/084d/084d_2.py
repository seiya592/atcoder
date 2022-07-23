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


Q = II()

cnt = [0] * (10 ** 5 + 1)

for n in range(2,10**5+1):
    if cnt[n]:
        continue
    for i in range(n*2, 10**5 + 1, n):
        cnt[i] += 1

# cnt[n] = 0 → nは素数
ans = [0] * (10**5+1)
for i in range(3,10**5+1):
    ans[i] += ans[i-1]
    if i % 2 == 0:
        continue
    if cnt[i] == 0 and cnt[(i+1)//2] == 0:
        ans[i] += 1

for _ in range(Q):
    l, r = IIS()
    print(ans[r] - ans[l-1])