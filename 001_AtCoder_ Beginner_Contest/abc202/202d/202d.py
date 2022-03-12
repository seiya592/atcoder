# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

A,B,K = (map(int, input().split()))
a = A
b = B
k = K
tmp = ''
for i in range(A+B):
    C = combinations_count(a+b,a)
    per = a / (a + b)

    # if C < k:
    #     if k % C == 0:
    #         k = C
    #     else:
    #         k = k % C

    per2 = k / C

    if per >= per2:
        tmp += 'a'
        a -= 1
    else:
        tmp +='b'
        b -= 1
        k = per2 * k

    if a == 0:
        for i in range(b):
            tmp += 'b'
        break
    if b == 0:
        for i in range(a):
            tmp += 'a'
        break



print(tmp)


