import collections


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
S = LI(N)

ans = collections.defaultdict(int)

# for s in S:
#     ans[s] += 1

for s in S:
    if ans[s] == 0:
        print(s)
        ans[s] += 1
    else:
        print(f"{s}({ans[s]})")
        ans[s] += 1
