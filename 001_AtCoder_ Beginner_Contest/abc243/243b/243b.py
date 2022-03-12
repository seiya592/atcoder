def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
A = LIIS()
B = LIIS()
ans1 = 0
ans2 = 0

lst = set(A) & set(B)
for l in lst:
    if A.index(l) == B.index(l):
        ans1+=1
    else:
        ans2+=1

print(ans1)
print(ans2)