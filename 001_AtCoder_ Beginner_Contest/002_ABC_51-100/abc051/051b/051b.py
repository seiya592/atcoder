def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


K, S = IIS()
ans = 0
for i in range(K+1):
    for j in range(K+1):
        if 0<=S - (i + j) <= K:
            ans += 1
print(ans)