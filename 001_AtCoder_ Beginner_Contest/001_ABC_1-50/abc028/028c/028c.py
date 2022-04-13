def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


A = LIIS()
t = set()
for a in A:
    for b in A:
        for c in A:
            if a != b and b != c and a != c:
                t.add(a+b+c)

a = sorted(list(t))
print(a[-3])