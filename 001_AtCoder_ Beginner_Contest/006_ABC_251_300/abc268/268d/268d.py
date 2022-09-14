"""
2022/09/10 20:45:51
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
import itertools
sys.setrecursionlimit(500000)
INF = 10**17
def has_bit(n, i) -> bool:
    """
    nで表現される集合に要素iが含まれているかを判定
    :param int n: 集合
    :param int i: 要素
    :return:bool True→含まれている False→含まれていない
    """
    return (n & (1 << i)) > 0

N,M = IIS()
S = LI(N)
T = LI(M)
T_SET = set(T)
# T_SET = [set() for _ in range(17)]
# for t in T:
#     d = len(t)
#     if len(t) <= 16:
#         a = t
#     else:
#         a = t[:16]
#     # a = t if len(t) <= 16 else t[:16]
#     T_SET[a.count('_')].add(a)

def dfs(s,t,n):
    if n == N:
        if 3<= len(t) <= 16:
            if t not in T_SET:
                print(t)
                exit()
        return

    for i in range(1,16):
        tt = t + '_'*i + s[n]
        if len(tt) > 16:
            break
        dfs(s,tt,n+1)


for s in itertools.permutations(S,N):
    dfs(s,s[0],1)
print(-1)
# for ss in itertools.permutations(S,N):
#     t = ss[0]
#     _LIST = [0] * 16
#     for s in ss[1:]:
#         _LIST[len(t)] = True
#         t += '_' + s
#
    # if len(t)>16:
    #     continue
    # while :
    #     if t not in T_SET:
    #         print(t)
    #         exit()

# print(-1)

# ALL = N**2
#
# for n in range(ALL):
#     t = ''
#     cnt = 0
#     for i in range(N):
#         if has_bit(n,i):
#             if t:
#                 t += '_' + S[i]
#                 cnt += 1
#             else:
#                 t = S[i]
#
#     if 3<=len(t)<=16:
#         if t not in T_SET[cnt]:
#             print(t)
#             exit()
# print(-1)