import itertools


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]
INF = 10**20


N = II()
K = II()
A = []
for _ in range(N):
    a = I()
    A.append(a)

ans = set()
for p in itertools.permutations(A,K):
    tmp = ''
    for i in range(K):
        tmp += p[i]
    ans.add(tmp)
print(len(ans))