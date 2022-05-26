def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import string
import copy
N, K = IIS()
S = list(I())
SS = copy.deepcopy(S)
checge = 1
for i in range(N):
    if not checge:
        break


    for s in string.ascii_lowercase:
        t = -1
        if s == S[i]:
            break

        for j in range(N):
            if S[j] == s:
                t = j

        if i < t:
            S[i], S[t] = S[t], S[i]

            f = 0
            for a,b in zip(S,SS):
                if a != b:
                    f += 1
            if f > K:
                S[i], S[t] = S[t], S[i]
                checge = 0
            else:
                checge = 1
                break

print(''.join(S))


