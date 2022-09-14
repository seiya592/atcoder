"""
2022/08/13 20:53:44
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


R,C = IIS()

def W():
    print('white')
    exit()

if R == 2 or R == 14:
    if 2<=C<=14:
        W()

if R == 4 or R == 12:
    if 4<=C<=12:
        W()

if R == 6 or R == 10:
    if 6<=C<=10:
        W()

if R == 8:
    if C == 8:
        W()

R,C = C,R

if R == 2 or R == 14:
    if 2<=C<=14:
        W()

if R == 4 or R == 12:
    if 4<=C<=12:
        W()

if R == 6 or R == 10:
    if 6<=C<=10:
        W()

if R == 8:
    if C == 8:
        W()

print('black')