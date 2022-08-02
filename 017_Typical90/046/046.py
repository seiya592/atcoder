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


N = II()
A = LIIS()
B = LIIS()
C = LIIS()
A = [i % 46 for i in A]
B = [i % 46 for i in B]
C = [i % 46 for i in C]
Ac = [0] * 46
Bc = [0] * 46
Cc = [0] * 46

for a in A:
    Ac[a] += 1

for b in B:
    Bc[b] += 1

for c in C:
    Cc[c] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k) % 46 != 0:
                continue
            ans += Ac[i] * Bc[j] * Cc[k]
print(ans)