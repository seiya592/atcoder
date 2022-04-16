def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N, K = IIS()
if K == 1:
    print('Infinity')
    exit()

def calc(x1,y1,x2,y2):
    p1=(x1,y1)
    p2=(x2,y2)
    a=p2[1]-p1[1]
    b=p1[0]-p2[0]
    c=p1[1]*p2[0]-p1[0]*p2[1]
    # -b = a+c // b
    if b == 0:
        return a,10**10,10**10
    return a//-b,-b,c//-b

XY = LLIIS(N)

ans = set()
for i,xy1 in enumerate(XY):
    for j, xy2 in enumerate(XY):
        count = 1
        a,b,c = calc(xy1[0],xy1[1],xy2[0],xy2[1])
        if b == 10**10 and c == 10**10:
            ans.add('00')
            continue
        for k, xy3 in enumerate(XY):
            if j == k:
                continue
            # if a*xy3[0] + b*xy3[1] + c == 0:
            if a*xy3[0] + c == xy3[1]:
                count += 1
        if count >= K:
            if a == 0:
                ans.add('0')
            elif c == 0:
                ans.add('c')
            else:
                ans.add((a,c))
            # if a == 0:
            #     ans.add('A')
            # elif b == 0:
            #     ans.add('B')
            # else:
            #     ans.add((a,b,c))
print(len(ans))