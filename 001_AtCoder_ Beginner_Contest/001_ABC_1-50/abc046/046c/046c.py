"""
2022/09/13 17:04:20
"""
import math


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


a = 1
b = 1

for _ in range(II()):
    T,A = IIS()

    # c = max(math.ceil(a / T) if a % T else a // T, math.ceil(b / A) if b % A else b // A)     # 誤差が出る
    c = max(-(-a//T), -(-b//A))
    a = T * c
    b = A * c
print(a+b)