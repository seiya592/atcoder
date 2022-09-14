"""
2022/09/03 20:35:09
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
if S == 'Monday':
    print(5)
elif S == 'Tuesday':
    print(4)
elif S == 'Wednesday':
    print(3)
elif S == 'Thursday':
    print(2)
elif S == 'Friday':
    print(1)