def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)

N,K = IIS()
A = LIIS()
B = LIIS()

Am = max(A)
l = []
for i,a in enumerate(A):
    if a == Am:
        l.append(i+1)

flg = False
for ll in l:
    if ll in B:
        flg = True

print('Yes' if flg else 'No')