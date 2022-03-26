def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


A = II()
B = II()
C = II()
D = II()

ans = A if A < B else B
ans += C if C < D else D
print(ans)