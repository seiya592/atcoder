import collections


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10


N,K = IIS()
A = LIIS()

s = set()
d = collections.defaultdict(int)
right = 0
left = 0
ans = 0
while right < N:
    s.add(A[right])
    d[A[right]] += 1


    while K < len(s):
        d[A[left]] -= 1
        if not d[A[left]]:
            s.remove(A[left])
        left += 1

    ans = max(ans, right-left+1)
    right += 1
print(ans)
