def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja

NX = []

while True:
    n,x = LIIS()
    if n == 0 and x == 0:
        break
    NX.append([n,x])

for n, x in NX:
    ans = 0
    for i in range(1,n):
        for j in range(i+1, (n + 1)):
            tmp = x - (i + j)
            if j < tmp <= n:
                ans += 1
    print(ans)