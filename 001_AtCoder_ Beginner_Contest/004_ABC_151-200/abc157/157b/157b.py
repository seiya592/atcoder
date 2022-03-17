def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))


A = [LIIS() for _ in range(3)]
N = II()
b = [II() for _ in range(N)]

BNG = [[False] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            BNG[i][j] = True


for i in range(3):
    flg = True
    for j in range(3):
        if not BNG[i][j]:
            flg = False
            break
    if flg:
        print('Yes')
        exit()

for j in range(3):
    flg = True
    for i in range(3):
        if not BNG[i][j]:
            flg = False
            break
    if flg:
        print('Yes')
        exit()

if BNG[0][0] and BNG[1][1] and BNG[2][2]:
    print('Yes')
    exit()

if BNG[2][0] and BNG[1][1] and BNG[0][2]:
    print('Yes')
    exit()


print('No')