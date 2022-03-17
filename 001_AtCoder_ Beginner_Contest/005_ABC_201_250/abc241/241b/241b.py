def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

N, M = IIS()
A = LIIS()
B = LIIS()

for b in B:
    try:
        A.remove(b)
    except ValueError:
        print('No')
        exit()

print('Yes')