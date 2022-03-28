def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import numpy as np

N, M = IIS()
A = LIIS()
C = LIIS()

A_poly = np.poly1d(A[::-1])     # 最高次の項が0番目
C_poly = np.poly1d(C[::-1])

B_poly = C_poly / A_poly
ans = B_poly[0].coef[::-1]   # 商の0次項から出力  B_poly[0]→商　B_poly[1]→余
print(' '.join(list(map(lambda x: str(int(x)), ans))))          # float→int→str