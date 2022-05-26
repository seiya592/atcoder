import itertools


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]
INF = 10**20


N = II()
A = LIIS()
B = LIIS()
total = 0
win = 0
for a in itertools.permutations(range(N)):
    total += 1

    a_win = 0
    b_Win = 0
    for i in range(N):
        if A[a[i]] > B[i]:
            a_win += 1
        elif A[a[i]] < B[i]:
            b_Win += 1

    if a_win > b_Win:
        win += 1

print(win / total)
# for a in itertools.permutations(range(N)):
#     for b in itertools.permutations(range(N)):
#         total += 1
#
#         a_win = 0
#         b_Win = 0
#         for i in range(N):
#             if A[a[i]] > B[b[i]]:
#                 a_win += 1
#             elif A[a[i]] < B[b[i]]:
#                 b_Win += 1
#
#         if a_win > b_Win:
#             win += 1
#
# print(win / total)