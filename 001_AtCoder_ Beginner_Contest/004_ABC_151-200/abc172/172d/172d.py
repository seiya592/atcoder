from functools import lru_cache


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)

N = II()

div = [0] * (N+1)
for n in range(1,N+1):
    for a in range(n, N+1, n):  #a = nからnステップ毎の値 →　div[a]約数にnが含まれている
        div[a] += 1
ans = 0
for i in range(1,N+1):
    ans += i * div[i]

print(ans)