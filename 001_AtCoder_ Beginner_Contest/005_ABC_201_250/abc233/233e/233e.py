"""
2022/11/16 19:07:04
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


X = I()
ans = []
# 全ての桁を足す
tot = 0
for x in X:
    tot += int(x)

kuriage = 0
for x in reversed(X):
    ans.append(str((tot+kuriage)%10))
    kuriage = (tot+kuriage)//10
    tot -= int(x)
else:
    if kuriage:
        ans.append(str(kuriage))
print(''.join(reversed(ans)))
