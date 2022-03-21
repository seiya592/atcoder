def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, X, Y = IIS()
ans = 0
for i in range(1,N+1):
    if i % X ==0 or i % Y == 0:
       ans += 1

print(ans)