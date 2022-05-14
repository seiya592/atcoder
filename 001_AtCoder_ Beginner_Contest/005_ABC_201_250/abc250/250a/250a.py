def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


H,W = IIS()
R, C = IIS()
ans = 0
if H != R:
    ans += 1
if R != 1:
    ans += 1

if W != C:
    ans += 1
if C != 1:
    ans += 1

print(ans)