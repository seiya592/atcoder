def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
Aoki = 0
T = []

for _ in  range(N):
    a, b = IIS()
    Aoki += a
    T.append(a*2 +b)

T.sort(reverse=True)

ans = 0
Takahashi = 0
for t in T:
    if Aoki >= Takahashi:
        ans += 1
        Takahashi += t
    else:
        break

print(ans)