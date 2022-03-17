def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

N = II()

SP = [[i] + IS() for i in range(1, N + 1)]

sp = sorted(SP, key=lambda x: (x[1], -int(x[2])))

for s in sp:
    print(s[0])