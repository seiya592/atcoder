def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

V, A ,B, C = IIS()
nokori = V % (A+B+C)

if nokori - A < 0:
    print('F')
elif (nokori - A) - B < 0:
    print('M')
else:
    print('T')
