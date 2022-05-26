import copy


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


S = I()
T = I()

tmp = ''
for i in range(len(S)):
    if S[i] == '?':
        tmp += 'a'
    else:
        tmp += S[i]
tmp = list(tmp)

ans = []
for i in range(len(S) - len(T)+1):
    for j in range(len(T)):
        if not(S[i+j] == '?' or S[i+j] == T[j]):
            break
    else:
        t = copy.deepcopy(tmp)
        for j in range(len(T)):
            t[i+j] = T[j]
        t = ''.join(t)
        ans.append(t)



if ans:
    ans.sort()
    print(ans[0])
else:
    print('UNRESTORABLE')
