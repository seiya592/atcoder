def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


S = I()
T = I()

S = ''.join(sorted(S))
T = ''.join(sorted(T,reverse=True))

if S<T:
    print('Yes')
else:
    print('No')
