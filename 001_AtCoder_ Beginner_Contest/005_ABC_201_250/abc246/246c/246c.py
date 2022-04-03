def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, K, X = IIS()
A = LIIS()

A.sort(reverse=True)
sum_p = sum(A)
nokori = K
AA = []
for a in A:
    tmp =  a // X   #クーポンの割引が効率よく行える枚数
    if nokori >= tmp:
        sum_p -= tmp * X
        nokori -= tmp
        AA.append(a - (tmp*X))
    else:
        sum_p -= nokori * X
        nokori = 0
        print(sum_p)
        exit()

AA.sort(reverse=True)
for aa in AA:
    if nokori > 0:
        sum_p -= aa
        nokori -= 1
    else:
        print(sum_p)
        exit()

print(sum_p)