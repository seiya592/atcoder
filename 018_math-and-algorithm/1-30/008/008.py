def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, S = IIS()

ans = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if i+j <= S:
            ans += 1

print(ans)