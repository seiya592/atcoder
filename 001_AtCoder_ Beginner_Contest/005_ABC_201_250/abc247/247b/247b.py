def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)



N = II()
ST = []
S = []
T = []
for _ in range(N):
    s, t = IS()
    ST.append(s)
    ST.append(t)
    S.append(s)
    T.append(t)

for s, t in zip(S, T):
    ST.pop(ST.index(s))
    ST.pop(ST.index(t))
    if (s in ST) and (t in ST):
        print('No')
        exit()
    ST.append(s)
    ST.append(t)
else:
    print('Yes')