def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,Y = IIS()

for i in range(N+1):
    for j in range(N+1-i):
        if Y - (i*10000) - (j*5000) == 1000*(N-(i+j)):
            print(i,j,(N-(i+j)))
            exit()
print(-1,-1,-1)