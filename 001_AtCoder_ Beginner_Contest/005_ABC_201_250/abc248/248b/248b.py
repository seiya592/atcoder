def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


A,B,K = IIS()
count = 0
while True:
    if A >= B:
        print(count)
        exit()
    count += 1
    A *= K
