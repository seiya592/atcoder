def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

A, B , C, D = IIS()
if A < C:
    print('Takahashi')
elif C < A:
    print('Aoki')
elif D < B:
    print('Aoki')
else:
    print('Takahashi')
