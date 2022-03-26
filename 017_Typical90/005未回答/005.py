# def I(): return input().rstrip()
# def IS(): return input().split()
# def II(): return int(input())
# def IIS(): return map(int, input().split())
# def LIIS(): return list(map(int, input().split()))
# import sys
# sys.setrecursionlimit(10000000)
# import itertools
#
# N, B, K = IIS()
# C = LIIS()
#
# ans = 0
# for l in itertools.product(C):
#     tmp = int(''.join(map(str, l)))
#     if tmp % B == 0:
#         ans += 1
#
# print(ans % (10**9+7))