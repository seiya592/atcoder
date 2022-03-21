def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
from collections import  deque

N = II()
ans = [True] * (2 * N + 1)
while True:
    for i, a in enumerate(ans):
        if a:
            ans[i] = False
            print(i+1)
            sys.stdout.flush()
            break

    t = II()
    if t == 0:
        break
    ans[t-1] = False

