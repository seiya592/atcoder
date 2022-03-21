def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


S = IS()
T = IS()

if S[0] == T[0] and S[1] == T[1] and S[2] == T[2]:
    print('Yes')
    exit()

if S[0] != T[0] and S[1] != T[1] and S[2] != T[2]:
    print('Yes')
    exit()

print('No')