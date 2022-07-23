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


H,W,N,M = IIS()

F = [[0] * W for _ in range(H)]

for _ in range(N):
    a,b = IIS()
    F[a-1][b-1] = 1

for _ in range(M):
    c,d = IIS()
    F[c-1][d-1] = 2

ans = [[0] * W for _ in range(H)]
import itertools

for i, f in enumerate(F):
    ptr = 0
    for key, group in itertools.groupby(f,key=lambda x:(x==2)):
        d = list(group)
        if key:
            ptr += len(d)
        else:
            if 1 in d:
                for j in range(len(d)):
                    ans[i][ptr+j] = 1
            ptr += len(d)

F = [list(a) for a in zip(*F)]
ans = [list(a) for a in zip(*ans)]
for i, f in enumerate(F):
    ptr = 0
    for key, group in itertools.groupby(f,key=lambda x:(x==2)):
        d = list(group)
        if key:
            ptr += len(d)
        else:
            if 1 in d:
                for j in range(len(d)):
                    ans[i][ptr+j] = 1
            ptr += len(d)

print(sum([sum(a) for a in ans]))