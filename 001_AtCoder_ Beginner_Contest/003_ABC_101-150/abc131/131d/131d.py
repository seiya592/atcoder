def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
AB = LLIIS(N)

AB.sort(key=lambda x:x[1])

time = 0
for a, b in AB:
    if time + a <= b:
        time += a
    else:
        print('No')
        exit()
else:
    print('Yes')