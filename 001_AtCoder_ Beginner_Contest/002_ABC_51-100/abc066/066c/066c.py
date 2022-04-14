import collections


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
A = LIIS()

odd = []
even = []   #偶数

for i, a in enumerate(A):
    if i % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

if N % 2 == 0:
    odd = list(reversed(odd))
    ans = odd + even
else:
    even = list(reversed(even))
    ans = even + odd

print(*ans)