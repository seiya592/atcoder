def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
A = LIIS()
B = LIIS()
Q = II()

Alen = [0] * (N+1)
Blen = [0] * (N+1)
CK = [False] * (N+1)
at = set()
bt = set()
for i in range(N):

    at.add(A[i])
    bt.add(B[i])
    Alen[i] = len(at)
    Blen[i] = len(bt)

i = 0
As = set()
Bs = set()
Xorset = set()
for a in A:
    if a in As:
        continue

    As.add(a)

    if a in Xorset:
        #要素Bが追加しているので削除
        Xorset.remove(a)
    else:
        Xorset.add(a)

    while i < N:
        if B[i] in Bs:
            i+=1
        else:
            Bs.add(B[i])

            if B[i] in Xorset:
                Xorset.remove(B[i])
            else:
                Xorset.add(B[i])
            break

    CK[len(As)] = not(len(Xorset))
pass
# N = II()
# A = LIIS()
# B = LIIS()
# Q = II()
#
# Alen = [0] * N
# Blen = [0] * N
# CK = [False] * (N + 1)
#
# i = 0
# j = 0
# As = set()
# Bs = set()
# while i < N or j < N:
#     while i < N:
#         As.add(A[i])
#         Alen[i] = len(As)
#         i += 1
#         if Alen[i-2] != Alen[i-1]:
#             break
#
#     while j < N:
#         Bs.add(B[j])
#         Blen[j] = len(Bs)
#         j += 1
#         if Blen[j-2] != Blen[j-1]:
#             break
#
#     if Alen[i-1] == Blen[j-1]:
#         CK[Alen[i-1]] = (As == Bs)  #ここで時間かかってる
#     else:
#         if i == N:
#             while j < N:
#                 Bs.add(B[j])
#                 Blen[j] = len(Bs)
#                 j += 1
#         else:
#             while i < N:
#                 As.add(A[i])
#                 Alen[i] = len(As)
#                 i += 1

for _ in range(Q):
    x,y = IIS()
    x -= 1
    y -= 1
    if Alen[x] != Blen[y]:
        print('No')
    else:
        if CK[Alen[x]]:
            print('Yes')
        else:
            print('No')

