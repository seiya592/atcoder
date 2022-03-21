def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
ans = 0
for i in range(1, (N+1), 2):
    tmp = 0
    for j in range(1,(i+1)):
        if i % j == 0:
            tmp += 1
    if tmp == 8:
        ans += 1

print(ans)