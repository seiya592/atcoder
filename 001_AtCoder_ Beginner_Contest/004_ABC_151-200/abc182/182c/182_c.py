def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20


S = I()
N = sum([int(s) for s in S])

if N % 3 == 0:
    print(0)
    exit()

for i,s in enumerate('0'+S):
    for j,t in enumerate(S,start=1):
        if (N - int(s) - int(t)) % 3 == 0 and (N - int(s) - int(t)) and i!=j:
            if i == 0:
                print(1)
            else:
                print(2)
            exit()
print(-1)