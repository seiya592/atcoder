def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
A = LIIS()
B = LIIS()

A.sort()
B.sort()
ans = 0
for a, b in zip(A,B):
    ans += abs(a-b)

print(ans)