import math


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import math

for i in range(200):
    print(f'n={i} {2**i} 10**{math.ceil(math.log(2**i, 10))}')