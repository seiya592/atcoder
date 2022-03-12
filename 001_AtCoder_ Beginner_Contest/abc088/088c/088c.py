def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))


c = [LIIS() for _ in range(3)]

for i in range(2):
    if not(c[i][0] - c[i+1][0] == c[i][1] - c[i+1][1] == c[i][2] - c[i+1][2]):
        print('No')
        exit()

for i in range(2):
    if not(c[0][i] - c[0][i+1] == c[1][i] - c[1][i+1] == c[2][i] - c[2][i+1]):
        print('No')
        exit()

print('Yes')