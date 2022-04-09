def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)
import math
from decimal import Decimal

a, b, c = IIS()
da = Decimal(str(a))
db = Decimal(str(b))
dc = Decimal(str(c))
l = Decimal('2')
if da.log10() / l.log10() < dc.log10() / l.log10() * db:
    print('Yes')
else:
    print('No')