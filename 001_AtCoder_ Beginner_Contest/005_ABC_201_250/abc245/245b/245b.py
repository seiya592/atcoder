def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
A = LIIS()

for i in range(2001):
    if i not in A:
        print(i)
        exit()
else:
    print(2001)