def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


# https://atcoder.jp/contests/abc058/tasks/abc058_b

O = I()
E = I()
t = ''
for o, e in zip(O,E):
    t += o
    t += e

if len(O) > len(E):
    t += O[-1]


print(t)