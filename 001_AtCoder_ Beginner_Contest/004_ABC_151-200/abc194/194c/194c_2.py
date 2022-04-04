def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)
from collections import defaultdict

N = II()
A = LIIS()

d = defaultdict(int)
for a in A:
    d[a] += 1

ans = 0
for i in range(0,401):
    ia = i - 200
    for j in range(0,401):
        ja = j - 200
        ans += abs(ia-ja)**2 * (d[ia]*d[ja])
print(ans//2)

