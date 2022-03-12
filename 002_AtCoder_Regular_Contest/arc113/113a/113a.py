import itertools
import math

#
# # permList = list(itertools.permutations(range(1,K)))
#
# def make_divisors(n):
#     lower_divisors , upper_divisors = [], []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             lower_divisors.append(i)
#             if i != n // i:
#                 upper_divisors.append(n//i)
#         i += 1
#     return lower_divisors + upper_divisors[::-1]
#
# Ky = make_divisors(K)
#
# lst1 = []
# for i in Ky:
#     for j in Ky:
#         for k in Ky:
#             if i * j * k <= K:
#                 if sorted([i,j,k]) not in lst1:
#                     lst1.append(sorted([i,j,k]))
#
# print(lst1)

# Klist = list(range(1,K + 1))
# Klist = list(range(1,math.ceil(K **(1/2)) + 1))
# Klist1 = list(range(1,math.ceil(K **(1/2)) + 1))
# Klist2 = list(range(1,math.ceil(K **(1/2)) + 1))
# a = K - Klist1[-1]
# print(Klist)
# print(Klist1)
# print(Klist2)

# rtn = [0] * 4
# for i in Klist2:
#     for j in Klist1:
#         if i * j > K:
#             break
#         for k in Klist:
#             if i * j * k > K:
#                 break
#             else:
#                 rtn[0] += 1
#                 if Klist1[-1] < k:
#                     rtn[1] += 1
#                 if Klist2[-1] < k:
#                     rtn[2] += 1
#
#
# print(sum(rtn))
# a = list(itertools.combinations(seq,3))
K = int(input())
rtn = 0
for i in range(1,K + 1):
    for j in range(1,K + 1):
        if i * j > K: break
        rtn += K // (i * j)

print(rtn)
