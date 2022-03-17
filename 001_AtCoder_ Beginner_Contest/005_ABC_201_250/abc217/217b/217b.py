def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


S1 = I()
S2 = I()
S3 = I()


tmp = ['ABC','ARC','AGC','AHC']

tmp.remove(S1)
tmp.remove(S2)
tmp.remove(S3)

print(tmp[0])