def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
from copy import deepcopy

ALL = '0123456789'
N = II()
S = LLIIS(N)

# nを揃えるとして探索


ans = 10**10
for n in ALL:
    done = [False] * N
    time = 0
    tmp = 0
    while not all(done):
        for i, s in enumerate(S):
            if s[time] == n and not done[i]:
                done[i] = True
                break
        time += 1
        tmp += 1
        time %= 10
    ans = min(ans,tmp)
print(ans-1)