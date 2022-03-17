#18:23:25~
import math

N = int(input())
sq = math.ceil(math.sqrt(N))

rtn = N - 1

for i in range(2,sq + 1):
    if N % i == 0:
        if (i - 1) + ((N // i) - 1) < rtn:
            rtn = (i - 1) + ((N // i) - 1)

print(rtn)