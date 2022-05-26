import itertools


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]


#順列全探索で解いてみる
N = II()
A = LLIIS(N)
M = II()
# E = set()   # setのinは計算量が定数
NG = [[False]*N for _ in range(N)]
for _ in range(M):
    x,y = IIS()
    x -= 1
    y -= 1
    NG[x][y] = True
    NG[y][x] = True
    # E.add((x,y))
    # E.add((y,x))
INF = 10**20
ans = INF


for p in itertools.permutations(range(N)):
    # if any([(p[i],p[i+1]) in E for i in range(N-1)]):
    if any([NG[p[i]][p[i+1]] for i in range(N-1)]):
        continue     #NGの組み合わせが1つ以上でもあれば
    ans = min(ans,sum([A[p[i]][i] for i in range(N)]))
print(ans if ans != INF else -1)

