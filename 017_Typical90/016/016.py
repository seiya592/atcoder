def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
A, B, C = IIS()
ans = 10000
for i in range(0,10000):
    for j in range(0,10000-i):
        tmp = N-(A*i)-(B*j)
        if tmp < 0:
            break
        if tmp % C == 0:
            ans = min(ans, i + j + (tmp//C))

print(ans)
