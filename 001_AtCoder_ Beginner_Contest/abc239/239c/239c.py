import math
x1,y1,x2,y2 = (map(int, input().split()))

xLst = [1,2,2,1,-1,-2,-2,-1]
yLst = [2,1,-1,-2,-2,-1,1,2]

ans = math.sqrt(5)
Lst1 = []
Lst2 = []

for x, y in zip(xLst,yLst):
    Lst1.append([x1 + x,y1 + y])
    Lst2.append([x2 + x,y2 + y])

flg = False
for l in Lst1:
    if l in Lst2:
        flg = True

if flg:
    print('Yes')
else:
    print('No')