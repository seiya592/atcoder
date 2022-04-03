def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import math
import numpy
A, B = IIS()
a = numpy.array([A, B])
ans1 = math.sin(numpy.arctan2(a[0], a[1]))
ans2 = math.cos(numpy.arctan2(a[0], a[1]))
print('{:.8f}'.format(ans1), '{:.8f}'.format(ans2))