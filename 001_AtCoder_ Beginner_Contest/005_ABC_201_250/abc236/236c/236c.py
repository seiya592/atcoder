def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))


N, M = LIIS()
S = IS()
T = IS()

index = 0
for s in S:
    if s == T[index]:
        index += 1
        print('Yes')
    else:
        print('No')