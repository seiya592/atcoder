def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


S = list(I())
T = I()

# Tが存在するか確認する
f = -1
for i in range(len(S) - (len(T) - 1)):
    for j, t in enumerate(T):
        if S[i+j] != t and S[i+j] != '?':
            break
    else:
        f = i

if f == -1:
    print('UNRESTORABLE')
    exit()

for i, t in enumerate(T):
    S[f+i] = t

for i in range(len(S)):
    if S[i] == '?':
        S[i] = 'a'

print(''.join(S))
