def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_c

N = II()
AB = [LIIS() for _ in range(N)]

AB = sorted(AB,key=lambda x:x[0]+x[1],reverse=True)
takahashi = 0
aoki = 0
for i in range(N):
    if i % 2 == 0:
        takahashi += AB[i][0]
    else:
        aoki += AB[i][1]

print(takahashi - aoki)