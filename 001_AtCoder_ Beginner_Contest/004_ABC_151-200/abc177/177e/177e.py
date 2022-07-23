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

N = II()
A = LIIS()
MAX = max(A)
ex = [0] * (MAX + 1)
cnt = [0] * (MAX+1)
for a in A:
    ex[a] += 1

pairwise = True
setwise = True

for n in range(2,MAX+1):
    if cnt[n]:
        continue

    f = N
    for i in range(n,MAX+1,n):
        cnt[i] += 1
        if ex[i]:
            f -= ex[i]


    if f <= N-2:
        pairwise = False
    if f == 0:
        setwise = False

if pairwise:
    print('pairwise coprime')
elif setwise:
    print('setwise coprime')
else:
    print('not coprime')