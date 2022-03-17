def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()
E = [LIIS() for _ in range(M)]
E.sort(key=lambda x: -x[0])

ans = 0
b = 10 ** 10
for e in E:
    if not e[0] <= b < e[1]:
        ans += 1
        b = e[0]

print(ans)