def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10


N, K = IIS()
A = LIIS()
sA = sorted(A)

for k in range(K):
    setA = []
    setB = []
    for i in range(0+k,N,K):
        setA.append(A[i])
        setB.append(sA[i])
    setA.sort()
    if setA != setB:
        print('No')
        exit()
print('Yes')



# sortA = sorted(A)
# min = -1

# if K == 1:
#     print('Yes')
#     exit()
#
# for i in range(N-K):
#     if A[i] != sortA[i]:
#         j = i + K
#         while j < N:
#             if A[i] == sortA[j]:
#                 A[i], A[j] = A[j], A[i]
#                 break
#             j += K
#         else:
#             print('No')
#             exit()


            # A[j],A[j+K] = A[i+K],A[i]
            # if A[i] != sortA[i]:
            #     print('No')
            #     exit()
# for i in range(N-K,N):
#     if A[i] != sortA[i]:
#         print('No')
#         exit()
# print('Yes')


# A = []
# for i,t in enumerate(a):
#     A.append((t,i))
#
# sortA = sorted(a,key=lambda x:(x[0],x[1]))

# for i, (a, s) in enumerate(zip(A,sortA)):
#     if N - K < i:
#         break
#     if a[0] == s[0]:
#         continue
#     elif A[i][0] == sortA[i+K][0]:
#         continue
#     else:
#         print('No')
#         exit()
# print('Yes')
# ans = 0
# for i, (_, j) in enumerate(sortA):
#     if  i:
#         ans += 1
#
# print('Yes' if ans <)