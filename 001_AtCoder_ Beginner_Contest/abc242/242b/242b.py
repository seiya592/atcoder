def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

S = I()

tmp = 'abcdefghijklmnopqrstuvwxyz'
tmp = list(tmp)
cnt = []

for t in tmp:
    cnt.append(S.count(t))

for i,c in enumerate(cnt):
    for _ in range(c):
        print(tmp[i] , end='')

