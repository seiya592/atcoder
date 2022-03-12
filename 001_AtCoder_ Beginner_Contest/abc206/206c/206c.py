from typing import re

N = int(input())
A = list(map(int, input().split()))
import  math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

#総数
t = combinations_count(N,2)
A.sort()
s = 0
for i in range(len(A)):
    if i < s:
        continue

    tmp = A[i]
    j = 1
    while True:
        if len(A) <= i + j:
            break
        if tmp == A[i+j]:
            j += 1
        else:
            break

    if j > 1:
        t -= combinations_count(j,2)
        s = i + j
print(t)