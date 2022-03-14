def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b

N = II()
AB = [LIIS() for _ in range(N)]

AB = sorted(AB,key=lambda x:x[1])

now = 0
ans = 0
for a,b in AB:
    if a > now:
        ans += 1
        now = b

print(ans)