def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


S = I()
K = II()
N = len(S)

a = set()
for i in range(N-K+1):
    a.add(S[i:i+K])

print(len(a))