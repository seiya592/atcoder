from operator import mul
from functools import reduce
from scipy.special import perm

K = int(input())
S = input()
T = input()

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

#Sの点数
Stmp = list(range(0,10))
for i in range(4):
    Stmp[int(S[i])] *= 10

#Tの点数
Ttmp = list(range(0,10))
for i in range(4):
    Ttmp[int(T[i])] *= 10

#組み合わせ総数

TSperm = perm(((K*9)-8), 2,exact=True)
TSa = T + S
# print(TS)
win = 0

for i in range(1,10):
    for j in range(1,10):
        TS = TSa + str(i) + str(j)
        Stmp2 = list(Stmp)
        Ttmp2 = list(Ttmp)
        Stmp2[i] *= 10
        Ttmp2[j] *= 10
        if TS.count(str(i)) > K or TS.count(str(j)) > K:
            continue
        if sum(Stmp2) > sum(Ttmp2):
            if i == j:
                tmp3 = K - TSa.count(str(i))
                win += tmp3 * (tmp3 - 1)
            else:
                win += (K - TSa.count(str(i))) * (K - TSa.count(str(j)))

if win == 0:
    print(0)
else:
    print(win / TSperm)
# print(win)
# print(TSperm)
# print(Stmp)
# print(sum(Stmp))