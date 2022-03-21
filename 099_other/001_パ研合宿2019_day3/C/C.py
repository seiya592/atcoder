def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M= IIS()
A = [LIIS() for _ in range(N)]
ans = 0
for i in range(M-1):
    for j in range(i+1,M):
        tmp = 0
        for a in A:
            tmp += max(a[i], a[j])
        ans = max(ans, tmp)

print(ans)