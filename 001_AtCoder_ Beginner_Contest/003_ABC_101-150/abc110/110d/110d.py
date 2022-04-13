import string


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


S = I()
T = I()

d = {}
a = string.ascii_lowercase
for s, t in zip(S, T):
    if s in d:
        if d[s] == t:
            pass
        else:
            print('No')
            exit()
    else:
        if t in a:
            d[s] = t
            a = a.replace(t, '')
        else:
            print('No')
            exit()
print('Yes')