import itertools


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


S = I()
T = I()

SS = [[key, len(list(group))]for key, group in itertools.groupby(S)]
TT = [[key, len(list(group))]for key, group in itertools.groupby(T)]

if len(SS) != len(TT):
    NO()

for s, t in zip(SS,TT):
    if s[0] != t[0]:
        NO()

    if s[1] == t[1] or (s[1] >= 2 and s[1] <= t[1]):
        continue
    NO()
YES()

