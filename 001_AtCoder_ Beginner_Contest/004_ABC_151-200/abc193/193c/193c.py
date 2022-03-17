import math

N = int(input())

rtn = []
for i in range(2,math.ceil(math.sqrt(N)) + 1):
    tmp = 2
    while i ** tmp <= N:
        rtn.append(i ** tmp)
        tmp += 1
print(N - len(set(rtn)))
