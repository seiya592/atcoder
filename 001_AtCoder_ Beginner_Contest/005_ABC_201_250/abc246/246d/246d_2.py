def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
MAX = 10 ** 6 + 1

ans = 10**19
L = 0
R = MAX
while L <= R:
    a = L
    b = R
    t = a ** 3 + (a ** 2 * b) + (a * b ** 2) + b ** 3
    if N < t:
        R-=1
        ans = min(ans,t)
    elif N > t:
        L += 1
    else:
        print(N)
        exit()
print(ans)