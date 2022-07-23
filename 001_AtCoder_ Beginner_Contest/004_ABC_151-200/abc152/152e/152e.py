# def I(): return input().rstrip()
# def IS(): return input().split()
# def II(): return int(input())
# def IIS(): return map(int, input().split())
# def LIIS(): return list(map(int, input().split()))
# def LLIIS(n): return [LIIS() for _ in range(n)]
# def LI(n): return [I() for _ in range(n)]
# def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
# import sys
# sys.setrecursionlimit(500000)
# INF = 10**10
#
# N = II()
# A = LIIS()
#
# import math
#
# def factorization(n):
#     fact = []
#     for i in range(2, math.ceil(math.sqrt(n))):
#         if n % i == 0:
#             cnt = 0
#             while n % i == 0:
#                 cnt += 1
#                 n //= i
#             fact.append([i, cnt])
#
#     if n != 1:
#         fact[n] = 1
#
#     return fact
