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
INF = 10**20


S = I()

d = dict()
for i in range(1,10):
    t = str(i)
    d[t] = S.count(t)

if len(S) == 1:
    if S == '8':
        print('Yes')
    else:
        print('No')

if len(S) == 2:
    if int(S[0]+S[1]) % 8 == 0 or int(S[1]+S[0]) % 8 == 0:
        print('Yes')
    else:
        print('No')

import collections
a = collections.Counter(S)
pass

pass
# if len(S) > 2:
#     for i in range(112,1000,8):
#         s = str(i)
#         if '0' in s:
#             continue
#         e = dict()
#         for j in range(1, 10):
#             t = str(j)
#             e[t] = s.count(t)
#         for k in d:
#             if d[k] < e[k]:
#                 break
#         else:
#             print('Yes')
#             exit()
#     else:
#         print('No')