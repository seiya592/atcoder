"""
2022/09/03 20:35:13
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


S = I()

L = [1] * 7
if S[6] == '0':
    L[0] = 0

if S[3] == '0':
    L[1] = 0

if S[1] == '0' and S[7] == '0':
    L[2] = 0

if S[4] == '0':
    L[3] = 0

if S[8] == '0' and S[2] == '0':
    L[4] = 0

if S[5] == '0':
    L[5] = 0

if S[9] == '0':
    L[6] = 0

if S[0] == '1':
    NO()
f = False
f2 = False
for i in range(7):
    if L[i] == 1:
        if f2:
            YES()
        f = True
    if L[i] == 0 and f:
        f2 = True

NO()