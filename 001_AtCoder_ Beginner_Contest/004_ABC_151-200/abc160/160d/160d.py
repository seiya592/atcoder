def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

#　解説AC

N, X, Y = IIS()
ans = [0] * N
# 全探索

for i in range(1,N):
    for j in range(i+1,N+1):
        t = min(j-i, (abs(i-X) + abs(j-Y) + 1)) # 直接わたるか、 X-Y経由してわたるか
        ans[t] += 1

for a in ans[1:]:
    print(a)