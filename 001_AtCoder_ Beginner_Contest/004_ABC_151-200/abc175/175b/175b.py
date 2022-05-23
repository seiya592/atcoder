import abc


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
L = LIIS()
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):

            t = L[i] + L[j] + L[k]
            tt = max(L[i],L[j],L[k])

            s = set()
            s.add(L[i])
            s.add(L[j])
            s.add(L[k])

            if tt < t-tt and len(s) == 3:
                ans += 1
print(ans)