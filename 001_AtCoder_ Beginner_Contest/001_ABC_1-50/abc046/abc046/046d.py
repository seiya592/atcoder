"""
2022/09/16 19:52:58
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
INF = 10**17


S = I()
N = len(S)

mid = (N+1)//2

win, lose = 0, 0
for s in S[:mid]:
    if s =='p':
        lose += 1

for s in S[mid:]:
    if s == 'g':
        win += 1
print(win-lose)