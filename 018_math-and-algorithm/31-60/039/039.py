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


N, Q = IIS()
I = [0] * (N+2)

for _ in range(Q):
    l,r,x = IIS()
    I[l] += x
    I[r+1] -= x

for i in range(2,N+1):
    I[i] += I[i-1]

ans = [''] * (N-1)
for i in range(1,N):
    if I[i] > I[i+1]:
        ans[i-1] = '>'
    elif I[i] == I[i+1]:
        ans[i-1] = '='
    else:
        ans[i-1] = '<'
print(''.join(ans))