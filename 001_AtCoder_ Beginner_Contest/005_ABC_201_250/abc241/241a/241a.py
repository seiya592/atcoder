def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

a = LIIS()

ans = a[a[0]]

# for i,t in enumerate(a):
#     if t == 0:
#
#         break

print(a[ans])