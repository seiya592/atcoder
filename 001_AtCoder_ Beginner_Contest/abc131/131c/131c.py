#19:21:00~
import math

A,B,C,D = (map(int, input().split()))
Cnum = len(range(C,B))
i = A

def func(i,B,CD):
    if i < CD:
        i = CD
    elif i >= CD:
        i = CD * ((i // CD) + min(1, i % CD))
        # i = CD * (i // CD) + min(1,i % CD)

    if i > B:
        return 0
    else:
        return len(range(i, B + 1,CD))

#最小公倍数
def lcm(a,b):
    return int(a*b/math.gcd(a,b))


Cnum = func(A,B,C)
Dnum = func(A,B,D)
CDnum = func(A,B,lcm(C,D))

print((B - A + 1) - Cnum - Dnum + CDnum)




# gcd = math.gcd(C,D)
# i = A
# tmp = 0
# while i <= B:
#     if i % gcd == 0:
#         tmp += 1
#         i += gcd
#     else:
#         i += 1
# else:
