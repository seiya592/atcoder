"""
2022/08/06 20:51:50
"""
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


A = LIIS()

t = False
s = False

for i in range(5):
    if A.count(A[i]) == 2:
        t = True
    if A.count(A[i]) == 3:
        s = True

if t and s:
    YES()
NO()