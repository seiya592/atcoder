def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
T = I()

x = 0
y = 0
state = 0
for t in T:
    if t == 'S':
        s = state % 4
        if s == 0:
            x += 1
        elif s == 1:
            y -= 1
        elif s == 2:
            x -= 1
        elif s == 3:
            y += 1
    else:
        state += 1

print(f'{x} {y}')

