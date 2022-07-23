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

MAX = (N-1) * (N-2) // 2  # スター型のグラフ
MIN = 0

if not MAX>=K>=MIN:
    print(-1)
    exit()

ans = []

#スター型のグラフを成形
for i in range(2,N+1):
    ans.append((1, i))

cnt = MAX
for i in range(2,N):
    for j in range(i+1, N+1):
        if cnt == K:
            break
        cnt -= 1
        ans.append((i,j))
    if cnt == K:
        break

print(len(ans))
for i, j in ans:
    print(i,j)