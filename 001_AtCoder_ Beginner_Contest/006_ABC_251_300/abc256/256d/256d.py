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
LR = LLIIS(N)
LR.sort(key=lambda x:(-x[1],x[0]))

lst = [False] * (10**5*2+1)

for l,r in LR:
    for i in range(l,r):
        if not lst[i]:
            lst[i] = True
        else:
            break

left = 0
right = 0
flg = True
i = 0

while i < (10**5*2+1):
    if not lst[i]:
        pass
    else:
        if flg:
            left = i
            flg = False

    if not flg and not lst[i]:
        print(left,i)
        flg = True

    i += 1



