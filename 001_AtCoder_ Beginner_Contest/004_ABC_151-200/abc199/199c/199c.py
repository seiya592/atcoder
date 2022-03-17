# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import math
A,B = (map(int, input().split()))
rtn = 0


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

for i in range(A,B + 1):
    lst = make_divisors(i)
    lst.reverse()
    for num in lst[1:]:
        if i - num >= A:
            rtn = max(rtn,num)
            break

print(rtn)