def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,W = IIS()
A = LIIS()
A.append(0)
ans = set()
for a in range(N+1):
    for b in range(N+1):
        for c in range(N+1):
            if (a!=b or (a==N and b==N)) and (a!=c or (a==N and c==N)) and (c!=b or (c==N and b==N)):
                t = A[a] + A[b] + A[c]
                if 0< t <= W:
                    ans.add(t)
print(len(ans))